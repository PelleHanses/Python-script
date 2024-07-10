#!/usr/bin/python3
'''
handle_pdf.py

Creates a pdf from data.
The function can be included in other scripts like this:
    from handle_pdf import create_pdf
    result = create_pdf(pdf_content, pdf_data)
'''

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.units import inch
import io
from reportlab.lib.enums import TA_LEFT

def create_pdf_file(buffer, pdf_content, pdf_data, total_pages=0):
    # Function to create the PDF with page count
    styles = getSampleStyleSheet()
    header_style = styles['Title']
    header_style.alignment = TA_LEFT  # Set to left alignment

    content_style = styles['BodyText']
    content_style.fontSize = 10
    comment_style = styles['Italic']  # Define comment_style

    logo_path = "./logo.png"

    doc = SimpleDocTemplate(buffer, pagesize=A4)

    def header_and_footer(canvas, doc):
        canvas.saveState()
        month_year_width = canvas.stringWidth(pdf_content["period"], 'Helvetica-Bold', 10)
        page_info = f"Page {doc.page} ({total_pages})"
        page_info_width = canvas.stringWidth(page_info, 'Helvetica-Bold', 10)
        canvas.drawImage(logo_path, inch, A4[1] - inch, width=200, height=50, mask='auto')
        canvas.setFont('Helvetica-Bold', 10)
        canvas.drawString(A4[0] - inch - page_info_width, A4[1] - 0.55 * inch, page_info)
        canvas.setFont('Helvetica', 8)
        footer_text = f"Delivered by XYZ"
        footer_text_width = canvas.stringWidth(footer_text, 'Helvetica', 8)
        canvas.drawString(A4[0] - inch - footer_text_width, 0.5 * inch, footer_text)
        canvas.restoreState()

    elements = []
    elements.append(Spacer(1, 0.25 * inch))
    elements.append(Paragraph("Monthly report", header_style))
    elements.append(Paragraph(f"Period: {pdf_content['period']}", content_style))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Compilation", header_style))
    elements.append(Paragraph(f"Org: {pdf_content['org']}", content_style))
    elements.append(Paragraph(f"Total something: {pdf_content['some_data_total']}", content_style))
    elements.append(Paragraph(f"Average number: {pdf_content['average_someting']}", content_style))
    elements.append(Spacer(1, 12))

    entries = [[
        "Date", "Start - end time", "Nr participants", "Moderator/Guest", "Length (h:m)"
    ]] + [[
        data["date"], f"{data['start']} - {data['end']}", data["participants"],
        f"{data['moderators']}/{data['guests']}", data["length"]
    ] for data in pdf_data]

    elements.append(Paragraph("All occurrences", header_style))
    table = Table(entries, colWidths=[1.5 * inch, 1.5 * inch, 1.2 * inch, 1.2 * inch, 1.2 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    elements.append(Paragraph(f" ", comment_style))
    elements.append(Paragraph(f"Explanation", comment_style))
    elements.append(Paragraph(f"Some extra info", comment_style))

    doc.build(elements, onFirstPage=header_and_footer, onLaterPages=header_and_footer)

def create_pdf(pdf_content, pdf_data):
    pdf_file_name = "./your_file.pdf"

    buffer = io.BytesIO()
    create_pdf_file(buffer, pdf_content, pdf_data)
    buffer.seek(0)

    # Count the number of pages
    total_pages = 0
    for line in buffer.getvalue().split(b'\n'):
        if b'/Page' in line:
            total_pages += 1
    total_pages = total_pages - 2

    buffer = io.BytesIO()
    create_pdf_file(buffer, pdf_content, pdf_data, total_pages)

    with open(pdf_file_name, "wb") as f:
        f.write(buffer.getvalue())

    print("Rapporten sparad i filen " + pdf_file_name)
    return "PDF created successfully: " + pdf_file_name, pdf_file_name

## Start

pdf_content = {
    "org": "Active organisation name",
    "period": "2024-05",
    "some_data_total": "386",
    "average_someting": "24"
}
pdf_data = [
    {
        "date": "2024-05-06",
        "start": "11:42",
        "end": "13:48",
        "participants": "45",
        "moderators": "10",
        "guests": "35",
        "length": "2:06",
    },
    {
        "date": "2024-05-08",
        "start": "09:32",
        "end": "11:34",
        "participants": "10",
        "moderators": "2",
        "guests": "8",
        "length": "2:02",
    },
]

### Start
if __name__ == "__main__":
    create_pdf(pdf_content, pdf_data)
