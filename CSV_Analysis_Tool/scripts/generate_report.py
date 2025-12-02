# generate_report.py
import pandas as pd
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# 1. Load your CSV (change the file name if needed)
csv_path = Path("./data/diabetes.csv")   
df = pd.read_csv(csv_path)

# 2. Calculate stats
stats = df.describe(include='all').round(2)

# 3. Create PDF
pdf_path = Path("./report.pdf")
doc = SimpleDocTemplate(str(pdf_path), pagesize=A4)
elements = []
styles = getSampleStyleSheet()

# Title
elements.append(Paragraph("CSV Analysis Report", styles['Title']))
elements.append(Spacer(1, 12))
elements.append(Paragraph(f"File: {csv_path.name} | Rows: {len(df)} | Columns: {len(df.columns)}", styles['Normal']))
elements.append(Spacer(1, 20))

# Convert stats to table for PDF
data = [stats.columns.tolist()]  # header
data += stats.round(2).values.tolist()

table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 12),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ('GRID', (0,0), (-1,-1), 1, colors.black)
]))
elements.append(table)

doc.build(elements)
print(f"report.pdf generated successfully at {pdf_path.resolve()}")
