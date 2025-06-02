# Face Comparison Web App

---

## 🧠 Team Name & Member

**Team Name**: Mnitian\_Coder
**Team Member**: Govind Ram Mali

---

## 🎯 Problem Statement / Objective

Build an app that can compare faces across two or more images and identify which faces match and which are different.
The system should:

* Detect faces in each image.
* Compare facial features using deep learning.
* Assign unique IDs to individuals.
* Highlight duplicates or unique individuals across all photos.
* Generate annotated images and a downloadable match report.

---

## 🛠 Tools & Technologies Used

| Category      | Tools & Libraries                     |
| ------------- | ------------------------------------- |
| Backend       | Python, Flask, DeepFace, OpenCV       |
| Frontend      | React.js, HTML, CSS, JavaScript       |
| Tunneling     | pyngrok                               |
| Face Matching | Facenet (DeepFace), Cosine Similarity |
| Data Format   | pandas, CSV                           |
| Environment   | Python 3.8+, VS Code                  |

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/face-comparison-app.git
cd face-comparison-app
```

### 2. Install Python Dependencies

Ensure Python 3.8 or above is installed.

```bash
pip install -r requirements.txt
pip install pyngrok
```

### 3. Run the Flask Server

```bash
python app.py
```

This will start a local Flask server and expose it using ngrok.
You'll see something like:

```
 * ngrok tunnel available at: http://abcd1234.ngrok.io
```

### 4. Update Frontend API URL

Open your frontend `index.html` or React component and **replace the existing API URL** with the new one from ngrok:

```javascript
const API_URL = "http://abcd1234.ngrok.io/compare";  // Use your actual tunnel URL
```

Do this each time you rerun `python app.py`.

### 5. Launch the Frontend

If using React:

```bash
npm install
npm start
```

Or if using static HTML:

* Open `index.html` in your browser, or
* Use VS Code Live Server Extension.

### 6. Use the App

* Upload 2 or more images with faces.
* Click **"Compare"**.
* View:

  * Annotated images with face IDs (e.g., "image1 - ID: 3").
  * A tabular match report showing which face in one image matches a face in another. Example:

    * *image1 - ID: 3* matched with *image2 - ID: 2* → **Match: Yes**
    * *image1 - ID: 1* has no match in image2 → **Match: No**
  * Downloadable CSV report including match details.

---

## 🖼 Screenshots

### 🔍 Annotated Face Detection Output

*(Add your image here)*

### 📊 CSV Report Preview

| Face ID (Image) | Matched With (Image) | Distance | Match |
| --------------- | -------------------- | -------- | ----- |
| 3 (Image 1)     | 2 (Image 2)          | 0.34     | Yes   |
| 1 (Image 1)     | —                    | —        | No    |

---

## 📂 Project Structure

```
├── app.py                # Flask backend
├── index.html / React    # Frontend UI
├── requirements.txt      # Python dependencies
├── face_compare.ipynb    # Optional notebook
├── screenshots/          # For storing screenshot images
└── README.md             # Project documentation
```

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for more information.
