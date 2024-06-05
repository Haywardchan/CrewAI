import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

try:
    # Run the command and redirect to a text file
    subprocess.run("poetry run financial_analyst_crew > output.txt", shell=True, check=True)

    # Convert the text file to a PDF
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate("output.pdf", pagesize=letter)
    elements = []

    with open("output.txt", "r") as f:
        for line in f:
            elements.append(Paragraph(line, styles["BodyText"]))

    doc.build(elements)
    print("PDF file created: output.pdf")

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")