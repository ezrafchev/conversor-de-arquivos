
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Converted Text to PDF', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def convert_txt_to_pdf(txt_file, pdf_file):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    with open(txt_file, 'r') as file:
        title = os.path.basename(txt_file)
        body = file.read()

    pdf.chapter_title(title)
    pdf.chapter_body(body)
    pdf.output(pdf_file)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Convert text files to PDF.')
    parser.add_argument('input', help='Input text file')
    parser.add_argument('output', help='Output PDF file')
    args = parser.parse_args()

    convert_txt_to_pdf(args.input, args.output)

