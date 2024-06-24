import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from format_txt import format_txtoutput
import requests

try:
    # Run the command and redirect to a text file
    subprocess.run("poetry run financial_analyst_crew > output.txt", shell=True, check=True)
    # Format the pdf file
    format_txtoutput()
    # Convert the text file to a PDF
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(name='CustomStyle', fontSize=10, leading=14)
    header_style = ParagraphStyle(
        name='Header',
        parent=styles['Heading1'],
        fontSize=16,
        leading=20,
        spaceAfter=12,
        alignment=1  # Center alignment
    )
    doc = SimpleDocTemplate("output.pdf", pagesize=letter)
    elements = []

    with open("output_after_extraction.txt", "r") as f:
        with open("output.md", "w") as file:
            # text = f.read()
            # text.replace("Task Output", PageBreak())
            for line in f:
                words = line.split()
                if line.startswith("Task output:"):
                    if elements:
                        elements.append(PageBreak())
                        file.write('\n')
                    elements.append(Paragraph(line.replace("Task output: ", ""), header_style))
                    file.write(line.replace("Task output: ", ""))
                elif len(words) > 1:
                    elements.append(Paragraph(line, custom_style))
                    file.write(line)

    doc.build(elements)
    print("PDF file created: output.pdf")

    # Set up API endpoints
    url = 'http://192.168.230.186:3001/api'
    with open('output.md', 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files, verify=False)
    if response.status_code == 200:
        print('File Uploaded successfully')
    else:
        print('File has not been uploaded')
    
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

