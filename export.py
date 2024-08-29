import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from format_txt import format_txtoutput
from flask import Flask, request, render_template_string
from flask_restful import Api, Resource
import sys
from src.financial_analyst_crew.main import run

# Set up an API for fetching the result from the backend
app = Flask(__name__)
api = Api(app)

class CrewAI_API(Resource):
    def get(self, query):
        # export(query)
        with open('output.md', 'r') as f:
            md = f.read()
        return {'res': render_template_string(md)}, 201
    
api.add_resource(CrewAI_API, '/api/res/<string:query>')

def export(query):
    try:
        # Run the command and redirect to a text file
        subprocess.run(f"poetry run financial_analyst_crew {query} > output.txt", shell=True, check=True)

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
                    elif len(words) == 0:
                        file.write(line)

        doc.build(elements)
        print("PDF file created: output.pdf")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__=='__main__':
    app.run(debug=True, port=5001)
