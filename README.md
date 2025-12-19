# AI Resume Matcher & Optimizer
A full-stack web application that uses OpenAI's GPT-4o-mini to analyze resumes against job descriptions, providing real-time feedback and keyword optimization.

##  Features
- **PDF Parsing:** Extracts raw text from resumes using `pdfplumber`.
- **AI Analysis:** Leverages GPT-4o-mini to calculate match scores and identify missing keywords.
- **Asynchronous UI:** Built with Flask and Tailwind CSS, using AJAX (Fetch API) for a seamless user experience.
- **Security:** Implements `.env` management to protect sensitive API credentials.

##  Tech Stack
- **Backend:** Python, Flask
- **AI/ML:** OpenAI API
- **Frontend:** JavaScript (ES6+), Tailwind CSS, HTML5
- **DevOps:** Virtual Environments (venv), Dotenv

##  Installation & Setup
1. Clone the repo: `git clone https://github.com/yourusername/resume-ai-checker`
2. Create a `.env` file and add your `OPENAI_API_KEY`.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `python app.py`
