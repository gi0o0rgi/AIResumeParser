import pdfplumber;

def extract_from_pdf(file_path):
    text = ""
    #Open up the PDF
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text
if __name__ == "__main__":
    resume_path = "resume.pdf"
    try:
        raw_text = extract_from_pdf(resume_path)
        print("--- EXTRACTED TEXT START ---")
        print(raw_text)
        print("--- EXTRACTED TEXT END ---")
        
        # Save it to a text file just to see the result clearly
        with open("extracted_text.txt", "w", encoding="utf-8") as f:
            f.write(raw_text)
            
    except FileNotFoundError:
        print(f"Error: Could not find '{resume_path}'. Is it in the same folder?")