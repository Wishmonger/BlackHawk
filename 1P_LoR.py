from docx import Document
import os

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Inches, Pt, Cm

def create_1P_LoR():
    doc = Document()

    table = doc.add_table(rows=1, cols=2)
    cell_left = table.cell(0, 0)
    cell_right = table.cell(0, 1)
    paragraph_left = cell_left.paragraphs[0]
    paragraph_left.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    run_left = paragraph_left.add_run()
    run_left.add_picture("Blackhawk_logo.jpg")
    paragraph_right = cell_right.paragraphs[0]
    paragraph_right.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
    run_right = paragraph_right.add_run("1670 Riviera Ave Suite 101\nWalnut Creek, CA 94596\nT: 925.736.9990 | F: 925.984.2621")
    run_right.font.name = 'Tahoma'
    run_right.font.size = Pt(9)
    heading = doc.add_heading("", 0)

    doc.save("1P_LoR.docx")


create_1P_LoR()