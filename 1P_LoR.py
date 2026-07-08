from docx import Document
import os

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Inches, Pt, Cm
import datetime
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn
from pprint import pprint
import re
import phonenumbers

def get_Today():
    date = datetime.date.today().strftime('%B %m %Y')
    return date

def insertHR(paragraph):
    p = paragraph._p  # p is the <w:p> XML element
    pPr = p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    pPr.insert_element_before(pBdr,
        'w:shd', 'w:tabs', 'w:suppressAutoHyphens', 'w:kinsoku', 'w:wordWrap',
        'w:overflowPunct', 'w:topLinePunct', 'w:autoSpaceDE', 'w:autoSpaceDN',
        'w:bidi', 'w:adjustRightInd', 'w:snapToGrid', 'w:spacing', 'w:ind',
        'w:contextualSpacing', 'w:mirrorIndents', 'w:suppressOverlap', 'w:jc',
        'w:textDirection', 'w:textAlignment', 'w:textboxTightWrap',
        'w:outlineLvl', 'w:divId', 'w:cnfStyle', 'w:rPr', 'w:sectPr',
        'w:pPrChange'
    )
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '1')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), 'auto')
    pBdr.append(bottom)

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


def get_email():
    response_email = True
    while response_email:
        response = input("Please enter the e-mail address of the client's insurance\n")
        if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", response):
           response_email = False
           return response
        else:
            pprint(f'You responded with {response}. My basic validation determined it is not a valid e-mail address. Please try again.\n')

def get_facsimile():
    response_facsimile = True
    while response_facsimile:
        response = input("Please enter the Fax Number of the client's insurance. Ignore the 1 in front.\n")
        parsed_Object = phonenumbers.parse(response, 'US')
        if phonenumbers.is_valid_number(parsed_Object):
            formatted = phonenumbers.format_number(parsed_Object, 'US')
            pprint(formatted)
            return(formatted)
        else:
            pprint(f'You responded with {response}. My validation determined it was not a legitimate number. Please try again.\n')

def get_type():
    response_Type = True
    while response_Type:
        response = input("Are you sending this letter through email or facsimile?\n")
        try:
            if response.lower() == 'email':
                response_Type = False
                return('email')
            elif response.lower() == 'facsimile' or response.lower() == 'fax':
                response_Type = False
                return('facsimile')
            else:
                pprint("Please enter either 'email' or 'facsimile'")
        except:
            pprint("Please enter only enter email or facsimile")


def create_1P_LoR():
    doc = Document()
    create_Blackhawk_header(doc)
    starting_Para = doc.add_paragraph('\n'+get_Today()+'\n')
    type = get_type()
    facsimile_or_email = ''
    if type == 'email':
        facsimile_or_email = get_email()
    elif type == 'facsimile':
        facsimile_or_email = get_facsimile()


    starting_Para.add_run(type+" "+str(facsimile_or_email))




    doc.save("1P_LoR.docx")


create_1P_LoR()