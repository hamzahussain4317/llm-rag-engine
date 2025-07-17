import fitz

def extract_text_from_pdf(file_path:str)->str:
    doc=fitz.open(file_path)
    full_text=""
    for i,page in enumerate(doc):
        full_text+=f"\n\n--- Page{i+1} ---\n\n"
        full_text+=page.get_text()
        
    return full_text.strip()