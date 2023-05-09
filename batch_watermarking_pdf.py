from pathlib import Path
#from PyPDF2 import PdfMerger, PdfReader
import PyPDF2

input_folder = Path(__file__).parent / "input"
output_folder = Path(__file__).parent / "output"

pdf_files = list(input_folder.glob("*.pdf"))

for file in pdf_files:

    filepath = Path(file)
    filename = filepath.name

    input = file
    watermark = Path(__file__).parent / "watermark.pdf"

    input_file = open(input, 'rb')
    input_pdf = PyPDF2.PdfReader(input_file)

    watermark_file = open(watermark, 'rb')
    watermark_pdf = PyPDF2.PdfReader(watermark_file)

    output = PyPDF2.PdfWriter()

    for i in range(len(input_pdf.pages)):
        page = input_pdf.pages[i]
        page.merge_page(watermark_pdf.pages[0])
        output.add_page(page)

    output_file = open(str(output_folder / f"{filename}"), 'wb')
    output.write(output_file)

    output_file.close()
    watermark_file.close()
    input_file.close()

#merger.write(str(pdf_output_dir / f"{key}.pdf"))
