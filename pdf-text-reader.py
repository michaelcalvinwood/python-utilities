import PyPDF2

def get_text_from_pdf (file_name):
    f = open(file_name,'rb')

    pdf_text = [0]  # zero is a placehoder to make page 1 = index 1

    pdf_reader = PyPDF2.PdfFileReader(f)

    for p in range(pdf_reader.numPages):        
        page = pdf_reader.getPage(p)
        pdf_text.append(page.extractText())

    f.close()
    return pdf_text