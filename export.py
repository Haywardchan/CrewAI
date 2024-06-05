import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from format_txt import format_txtoutput

try:
    # Run the command and redirect to a text file
    subprocess.run("poetry run financial_analyst_crew > output.txt", shell=True, check=True)
    # Format the pdf file
    format_txtoutput()
    # Convert the text file to a PDF
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(name='CustomStyle', fontSize=12, leading=14)
    doc = SimpleDocTemplate("output.pdf", pagesize=letter)
    elements = []

    with open("output.txt", "r") as f:
        for line in f:
            elements.append(Paragraph(line, custom_style))

    doc.build(elements)
    print("PDF file created: output.pdf")

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")