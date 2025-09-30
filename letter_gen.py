from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch

# Document path
doc_path = "/mnt/data/Thinking_Cybersecurity_Author_Contract_Filled.pdf"

# Styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle('TitleStyle', parent=styles['Title'], alignment=TA_CENTER, fontSize=16, spaceAfter=20)
subtitle_style = ParagraphStyle('SubtitleStyle', parent=styles['Heading2'], alignment=TA_CENTER, spaceAfter=12)
normal_style = styles["Normal"]

# Content
title = "Author Contract — Submission Confirmation"
subtitle = "Cambridge Scholars Publishing"

contract_body = """
This document confirms the author's acceptance of the Publishing Agreement and outlines the expected submission date for the final manuscript of the accepted title.

<b>Author Name:</b> Paulo H. Leocadio<br/>
<b>Primary Email:</b> ph@zinnia.holdings<br/>
<b>Title of Work:</b> <i>Thinking Cybersecurity: AI Automation through Diffused Intelligence</i><br/>
<b>Publisher:</b> Cambridge Scholars Publishing<br/>
<b>Estimated Manuscript Submission Date:</b> <b>26 March 2026</b><br/>
<b>Agreement Reference:</b> Acceptance email dated 26 September 2025 from Alison Duffy (Commissioning Editor)

The author confirms the intention to submit the completed manuscript on or before the proposed date above. All copyright permissions for third-party material will be obtained prior to submission.
"""

signature_block = """
<br/><br/><br/>
______________________________<br/>
<b>Signature of Author</b><br/>
Date: ________________________
"""

# Build PDF
doc = SimpleDocTemplate(doc_path, pagesize=LETTER,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=72)

elements = [
    Paragraph(title, title_style),
    Paragraph(subtitle, subtitle_style),
    Spacer(1, 0.25 * inch),
    Paragraph(contract_body, normal_style),
    Spacer(1, 0.5 * inch),
    Paragraph(signature_block, normal_style),
    PageBreak()
]

doc.build(elements)
doc_path
