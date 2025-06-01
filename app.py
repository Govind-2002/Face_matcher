# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok
import os
import tempfile
import cv2
import numpy as np
import pandas as pd
from io import BytesIO
import base64
from deepface import DeepFace

app = Flask(__name__)
CORS(app)

# Set up ngrok tunnel
public_url = ngrok.connect(5000)
print(f" * ngrok tunnel available at: {public_url}")

THRESHOLD = 0.50  # Cosine distance threshold for face similarity

def detect_and_encode_faces(img_path):
    face_embeddings = []
    face_regions = []

    try:
        representations = DeepFace.represent(
            img_path=img_path,
            model_name='Facenet',
            enforce_detection=False,
            detector_backend='opencv'
        )
    except Exception as e:
        print(f"[ERROR] DeepFace.represent failed: {e}")
        return [], []

    # Ensure representations is a list of dictionaries
    if isinstance(representations, dict):
        representations = [representations]
    elif not isinstance(representations, list):
        print(f"[ERROR] Unexpected type for representations: {type(representations)}")
        return [], []

    for face in representations:
        if isinstance(face, dict) and 'embedding' in face and 'facial_area' in face:
            embedding = np.array(face['embedding'], dtype=np.float32)
            norm = np.linalg.norm(embedding)
            print(f"Embedding norm: {norm}")
            if norm > 1e-6:
                region = face['facial_area']
                face_embeddings.append(embedding)
                face_regions.append(region)
            else:
                print("[WARN] Skipped zero-norm embedding")
        else:
            print(f"[WARN] Unexpected face format: {face}")

    return face_embeddings, face_regions

def annotate_image(image_path, regions, face_ids):
    img = cv2.imread(image_path)
    for region, face_id in zip(regions, face_ids):
        x, y, w, h = region['x'], region['y'], region['w'], region['h']
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, f"ID: {face_id}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    success, buffer = cv2.imencode(".jpg", img)
    return buffer.tobytes() if success else None

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1, dtype=np.float32)
    vec2 = np.array(vec2, dtype=np.float32)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return float('nan')
    return float(np.dot(vec1, vec2) / (norm1 * norm2))

@app.route('/compare', methods=['POST'])
def compare_faces():
    files = request.files.getlist('images')
    if len(files) < 2:
        return jsonify({'error': 'Please upload at least two images'}), 400

    all_embeddings = []
    all_regions = []
    all_paths = []
    face_index_map = []

    for img_idx, file in enumerate(files):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            file.save(tmp.name)
            embeddings, regions = detect_and_encode_faces(tmp.name)
            all_embeddings.extend(embeddings)
            all_regions.append(regions)
            all_paths.append(tmp.name)
            face_index_map.extend([(img_idx, i) for i in range(len(embeddings))])

    face_ids = [-1] * len(all_embeddings)
    current_id = 0
    for i in range(len(all_embeddings)):
        if face_ids[i] != -1:
            continue
        similarity = cosine_similarity(all_embeddings[i], all_embeddings[i])
        if np.isnan(similarity) or similarity == 0:
            continue
        face_ids[i] = current_id
        for j in range(i + 1, len(all_embeddings)):
            if face_ids[j] == -1:
                similarity = cosine_similarity(all_embeddings[i], all_embeddings[j])
                if not np.isnan(similarity) and similarity > (1 - THRESHOLD):
                    face_ids[j] = current_id
        current_id += 1

    # Annotate and encode each image
    annotated_b64 = []
    idx = 0
    for img_idx, regions in enumerate(all_regions):
        face_ids_img = face_ids[idx:idx+len(regions)]
        idx += len(regions)
        annotated_bytes = annotate_image(all_paths[img_idx], regions, face_ids_img)
        if annotated_bytes:
            annotated_b64.append(base64.b64encode(annotated_bytes).decode())
        os.remove(all_paths[img_idx])  # Clean up

    # Prepare CSV match report
    rows = []
    for i, (img_i, face_i) in enumerate(face_index_map):
        id_i = face_ids[i]
        for j, (img_j, face_j) in enumerate(face_index_map):
            similarity = cosine_similarity(all_embeddings[i], all_embeddings[j])
            rows.append({
                'Face ID (Image)': f"{id_i} (Image {img_i + 1})",
                'Matched With (Image)': f"{face_ids[j]} (Image {img_j + 1})" if i != j else '—',
                'Cosine Similarity': round(similarity, 4) if not np.isnan(similarity) else 'NaN',
                'Match': "Yes" if face_ids[i] == face_ids[j] and i != j else "No"
            })

    df = pd.DataFrame(rows)
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False)
    csv_str = csv_buffer.getvalue().decode()

    return jsonify({
        'annotated_images': annotated_b64,
        'match_report': df.to_dict(orient='records'),
        'csv_report': csv_str
    })

if __name__ == "__main__":
    app.run()
