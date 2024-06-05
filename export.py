import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from format_txt import format_txtoutput

try:
    # Run the command and redirect to a text file
    subprocess.run("poetry run financial_analyst_crew > output.txt", shell=True, check=True)
    # Format the pdf file
    format_txtoutput()
    # Convert the text file to a PDF
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(name='CustomStyle', fontSize=10, leading=14)
    doc = SimpleDocTemplate("output.pdf", pagesize=letter)
    elements = []

    with open("output_after_extraction.txt", "r") as f:
        # text = f.read()
        # text.replace("Task Output", PageBreak())
        for line in f:
            if line.strip()=="Task output:":
                elements.append(PageBreak())
            else:
                elements.append(Paragraph(line, custom_style))

    doc.build(elements)
    print("PDF file created: output.pdf")

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")