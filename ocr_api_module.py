# ocr_api_module.py

import fitz  # PyMuPDF

def extract_text_from_file(filepath):
    """Extract text from a PDF document."""
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text