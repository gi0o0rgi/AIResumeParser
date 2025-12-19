from flask import Flask, render_template, request, jsonify
import os
import json
from reader import extract_from_pdf
from analyzer import analyze_resume

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # 1. Get the data from the frontend form
    job_desc = request.form.get('job_description')
    file = request.files.get('resume')

    if not file or not job_desc:
        return jsonify({"error": "Missing file or job description"}), 400

    try:
        # 2. Save file temporarily
        file_path = "temp_resume.pdf"
        file.save(file_path)
        
        # 3. Extract text
        resume_text = extract_from_pdf(file_path)
        
        # 4. Get AI Analysis
        # This returns a JSON-formatted string from OpenAI
        raw_analysis_string = analyze_resume(resume_text, job_desc)
        
        # 5. Convert string to a Python Dictionary
        analysis_data = json.loads(raw_analysis_string)
        
        # Cleanup: remove the temp PDF file
        os.remove(file_path)

        # 6. Send the clean data back to the browser
        return jsonify(analysis_data)

    except Exception as e:
        if os.path.exists("temp_resume.pdf"):
            os.remove("temp_resume.pdf")
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)