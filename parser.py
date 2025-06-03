import pdfplumber

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        full_text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return full_text
