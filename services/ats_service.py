import io
from PyPDF2 import PdfReader

# ✅ Expanded ATS keyword list (soft + technical skills)
ATS_KEYWORDS = [
    # Soft skills
    "problem solving", "communication", "teamwork", "leadership",
    "conflict resolution", "strategic thinking", "time management",
    "decision making", "innovation", "adaptability", "collaboration",
    "analytical thinking", "critical thinking", "creativity", "initiative",
    
    # Technical skills
    "data analysis", "machine learning", "deep learning", "natural language processing",
    "python", "java", "c++", "c", "sql", "html", "css", "javascript",
    "react", "node.js", "flask", "django", "git", "github", "mongodb",
    "data structures", "algorithms", "object oriented programming", "database management",
    "tensorflow", "keras", "pandas", "numpy", "scikit-learn", "power bi", "excel"
]


def extract_text_from_pdf(file_bytes):
    """Extracts text from a PDF file uploaded via Streamlit"""
    try:
        with io.BytesIO(file_bytes) as pdf_file:
            reader = PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        return text.lower()
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""


def get_ats_score_from_pdf(file_bytes):
    """
    Takes uploaded PDF file bytes, extracts text, and computes ATS score.
    Returns a dictionary with 'score' and 'remarks'.
    """
    text = extract_text_from_pdf(file_bytes)
    if not text:
        return {"score": None, "remarks": "Unable to read text from PDF."}

    matched_keywords = [kw for kw in ATS_KEYWORDS if kw in text]
    score = round((len(matched_keywords) / len(ATS_KEYWORDS)) * 100)

    remarks = f"✅ Found {len(matched_keywords)} of {len(ATS_KEYWORDS)} key skills: {', '.join(matched_keywords[:10])}"
    return {"score": score, "remarks": remarks}
