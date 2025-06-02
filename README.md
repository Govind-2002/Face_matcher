Face Comparison Web App
This is a Flask-based face comparison tool powered by DeepFace that allows users to upload multiple images, automatically detect faces, compare them, assign unique IDs to matched faces, and visualize results with annotated images and a downloadable match report.

Team Details
Developer: Govind Ram Mali

Problem Statement
Build an app that can compare faces across two or more images and tell which faces match and which ones are different. You'll design a tool that detects faces, analyzes them, and highlights duplicates or unique individuals between photos.

Features
Upload 2 or more images

Detect all faces in each image

Assign unique IDs to matched faces

Compare using Facenet + Cosine similarity

Visual output with bounding boxes and IDs

Tabular match report with matching scores

Downloadable CSV match report

Tech Stack
Layer	Technologies Used
Backend	Python, Flask, DeepFace, OpenCV
Frontend	React.js, HTML, CSS, JavaScript
Tunneling	pyngrok
Matching	Facenet (DeepFace), Cosine Distance
Data	pandas, CSV

How to Run the Project Locally
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Govind-2002/Face_matcher.git
cd Face_matcher
2. Install Dependencies
Make sure Python ≥ 3.8 is installed.

bash
Copy
Edit
pip install -r requirements.txt
Also install pyngrok if not already:

bash
Copy
Edit
pip install pyngrok
3. Launch the Backend
Run the Flask app:

bash
Copy
Edit
python app.py
You’ll see a line like:

arduino
Copy
Edit
 * ngrok tunnel available at: http://abcd1234.ngrok.io
4. Update the Frontend API URL
Each time you run python app.py, you must copy the new ngrok link and update the following line in index.html:

js
Copy
Edit
const API_URL = "http://abcd1234.ngrok.io/compare";
5. Launch the Frontend
Option 1: Use VS Code Live Server Extension → Right-click index.html → "Go Live"

Option 2: Open index.html manually in your browser

6. Using the App
Select 2 or more face images

Click "Compare"

View results:

Annotated images with face IDs

Match report table

Option to Download CSV

Project Structure
bash
Copy
Edit
├── app.py                # Flask backend with DeepFace face comparison
├── index.html            # Frontend (React entry or HTML fallback)
├── requirements.txt      # Python dependencies
├── face_compare.ipynb    # (Optional) Notebook version of the app
└── README.md             # Project documentation
Sample Output
Annotated Image with IDs
Each detected face will be marked with a bounding box and a unique ID.

Match Report (CSV)
Sample report:

mathematica
Copy
Edit
Face ID (Image)   Matched With (Image)   Distance   Match
1 (Image 1)       1 (Image 2)            0.34       Yes
2 (Image 1)       —                      —          No

(Place your actual CSV screenshot image in a screenshots folder inside the repo)

License
This project is licensed under the MIT License. See the LICENSE file for more details.


