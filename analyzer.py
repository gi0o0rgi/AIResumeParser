import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the API key from the .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume_text, job_description):
    prompt = f"""
    Analyze the given resume against the job description. 
    Provide a Match Score (0-100), 3 missing keywords, and a 1-sentence career tip.
    Return the result ONLY as a JSON object with these keys: 
    'score', 'missing_keywords', 'tip'.

    JOB DESCRIPTION:
    {job_description}

    RESUME TEXT:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini", # Cheaper and faster for testing
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" } # Ensures valid JSON back
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    # Test with the text I extracter earlier
    with open("extracted_text.txt", "r") as f:
        my_resume = f.read()
    
    sample_job = "Indian bellydancing expert. Must know the intricacies of indian belly dancing."
    
    print("Analyzing...")
    result = analyze_resume(my_resume, sample_job)
    print(result)