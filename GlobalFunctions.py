from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Inches, Pt, Cm
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn
import datetime

from fpdf import FPDF

class CustomPDF(FPDF):
    def header(self):
        x = self.get_x()
        y = self.get_y()
        self.image('Blackhawk_logo.jpg', w=60, h=25)
        self.set_xy(x+180, y+10)
        self.set_font("helvetica", size=8)
        self.cell(10, 10,'1670 Riviera Ave Suite 101', align="Right")
        self.set_xy(x + 180, y+13)
        self.cell(10, 10, 'Walnut Creek, CA 94596', align="Right")
        self.set_xy(x + 180, y+16)
        self.cell(10, 10, 'T: 925.736.9990 | F: 925.984.2621', align="Right")
        self.ln(10)
        current_y = self.get_y()  # 5mm below the current text position
        start_x = self.l_margin  # Left margin
        end_x = self.w - self.r_margin  # Total page width minus right margin

        self.line(start_x, current_y, end_x, current_y)

        # 3. Move the cursor below the line before writing more text
        self.set_y(current_y + 5)



def create_Blackhawk_header(doc):
    section = doc.sections[0]
    header = section.header
    table = header.add_table(rows=1, cols=2, width=(Cm(16)))
    cell_left = table.cell(0, 0)
    cell_right = table.cell(0, 1)
    paragraph_left = cell_left.paragraphs[0]
    paragraph_left.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    run_left = paragraph_left.add_run()
    run_left.add_picture("Blackhawk_logo.jpg")
    paragraph_right = cell_right.paragraphs[0]
    paragraph_right.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
    run_right = paragraph_right.add_run(
        "\n\n1670 Riviera Ave Suite 101\nWalnut Creek, CA 94596\nT: 925.736.9990 | F: 925.984.2621")
    run_right.font.name = 'Tahoma'
    run_right.font.size = Pt(9)
    borders = OxmlElement('w:tblBorders')
    bottom_border = OxmlElement('w:bottom')
    bottom_border.set(qn('w:val'), 'single')
    bottom_border.set(qn('w:sz'), '4')
    borders.append(bottom_border)
    table._tbl.tblPr.append(borders)
def get_Today():
    date = datetime.date.today().strftime('%B %d, %Y')
    return date

#pyinstaller -F --add-data 'Blackhawk_logo.jpg;.' --add-data 'Samual LC Dollar Signature.jpg;.' --add-data 'AG Signature.JPG;.' --add-data 'Daniel Signature.png;.' --add-data 'jang.jpg;.'  .\Disbursement.py