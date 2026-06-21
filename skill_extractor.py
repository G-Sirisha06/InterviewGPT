# Import your text extractor function from the first file
from resume_parser import extract_resume_text

SKILLS = [
    "python", "sql", "machine learning", "deep learning", 
    "nlp", "pandas", "numpy", "tensorflow", "pytorch", 
    "langchain", "rag", "openai"
]

def extract_skills(text):
    found = []
    text = text.lower()
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return list(set(found))

if __name__ == "__main__":
    # Put the exact same path to your test resume here!
    pdf_file = r"C:/Users/G.GOWTHAM/OneDrive/Desktop/G.Sirisha/resume.pdf"

    # 1. Get the text
    resume_text = extract_resume_text(pdf_file)
    
    # 2. Extract the skills
    extracted_skills = extract_skills(resume_text)
    
    print("\n--- Extracted Skills From Resume ---")
    print(extracted_skills)