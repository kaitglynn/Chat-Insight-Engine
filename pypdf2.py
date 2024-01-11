```python
import PyPDF2

def process_pdf(file_path):
    try:
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages
        fileData = {"file_path": file_path, "num_pages": num_pages}
        return fileData
    except Exception as e:
        print("Error processing PDF: ", e)
        return None

def extract_text_from_pdf(fileData):
    try:
        pdf_file = open(fileData["file_path"], 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ""
        for page_num in range(fileData["num_pages"]):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text
    except Exception as e:
        print("Error extracting text from PDF: ", e)
        return None

def merge_pdfs(file_list, output_path):
    try:
        pdf_writer = PyPDF2.PdfFileWriter()
        for file_path in file_list:
            pdf_file = open(file_path, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page)
        with open(output_path, 'wb') as out:
            pdf_writer.write(out)
        print("PDFs merged successfully.")
    except Exception as e:
        print("Error merging PDFs: ", e)
```
