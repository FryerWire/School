
import PyPDF2

def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as GPT_Inputs:
        reader = PyPDF2.PdfReader(GPT_Inputs, strict = False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

    return pdf_text

extracted_text = extract_text_from_pdf("1-19_ARTH281_S23.pdf")

with open('GPT_Inputs.txt', 'w') as file:
    
    for item in extracted_text:
        file.write("%s\n" % item)
