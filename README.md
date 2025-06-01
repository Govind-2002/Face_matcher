# Face Comparison Web App

This is a Flask-based face comparison tool powered by DeepFace that allows users to upload multiple images, automatically detect faces, compare them, assign unique IDs to matched faces, and visualize results with annotated images and a downloadable match report.

---

## 🚀 Features

- Upload 2 or more images.
- Detect all faces in each image.
- Assign unique IDs to matched faces.
- Compare using *Facenet + Cosine similarity*.
- Annotated images with bounding boxes and face IDs.
- View tabular match report.
- Download CSV report with distances and match results.

---

## 📦 Tech Stack

| Layer     | Tools Used                         |
|-----------|------------------------------------|
| Backend   | Python, Flask, DeepFace, OpenCV    |
| Frontend  | HTML, CSS, JavaScript (vanilla)    |
| Tunneling | pyngrok                             |
| Matching  | Facenet (DeepFace), Cosine Distance |
| Data      | pandas, CSV                        |

---

## 🖥 How to Run Locally

### 1. Clone this repository

```bash
git clone https://github.com/your-username/face-compare-app.git
cd face-compare-app
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Ensure you have Python ≥ 3.8 and ngrok set up (pip install pyngrok)

3. Launch the Backend
Open face_compare.ipynb (or run app.py directly if you prefer):

bash
Copy
Edit
python app.py
You’ll see something like:

bash
Copy
Edit
 * ngrok tunnel available at: http://abcd1234.ngrok.io
4. Update Frontend with API URL
Open the index.html file and replace the line:

js
Copy
Edit
const API_URL = "http://localhost:5000/compare";
with:

js
Copy
Edit
const API_URL = "http://abcd1234.ngrok.io/compare";  // use your actual tunnel URL
5. Launch the Frontend
You can run the frontend in two ways:

Using VS Code Live Server Extension: Right-click index.html → "Go Live"

Or simply open index.html in your browser

6. Using the App
Drag and drop or select 2+ face images

Click "Compare"

View:

Annotated images with face IDs

Match Report Table

Option to Download CSV

📂 File Structure
bash
Copy
Edit
├── app.py                # Flask backend with DeepFace face comparison
├── index.html            # Frontend UI (HTML + JS)
├── requirements.txt      # Python dependencies
├── face_compare.ipynb    # (Optional) Notebook version of the app
└── README.md             # This file
🧪 Sample Output
Annotated Image

Bounding box with "ID: #"

Match Report (CSV)

Face ID (Image)	Matched With (Image)	Distance	Match
1 (Image 1)	1 (Image 2)	0.34	Yes
2 (Image 1)	—	—	No

✅ Status
✔ All core features implemented
✔ Tested locally
✔ Match accuracy validated
🟢 Ready for submission / deployment
