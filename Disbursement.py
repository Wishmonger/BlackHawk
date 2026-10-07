import pandas as pd
from PIL.ImageFont import truetype

from GlobalFunctions import  get_Today
from pprint import pprint
import traceback
from fpdf import FPDF
import sys
import os
import datetime
#os.chdir(sys._MEIPASS)
#os.system('included\\Blackhawk_logo.jpg')
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class CustomPDF(FPDF):
    def header(self):
        x = self.get_x()
        y = self.get_y()
        self.image(name=resource_path('Blackhawk_logo.jpg'), w=60, h=25)
        #self.set_xy(x+170, y+10)
        self.set_xy(x+10,y+10)
        self.set_font("Times", size=10)
        #self.cell(10, 10,'1670 Riviera Ave Suite 101', align="Right")
        #self.set_xy(x + 170, y+13)
        #self.cell(10, 10, 'Walnut Creek, CA 94596', align="Right")
        #self.set_xy(x + 170, y+16)
        #self.cell(10, 10, 'T: 925.736.9990 | F: 925.984.2621', align="Right")
        self.multi_cell(w=170, h=4, text='1670 Riviera Ave Suite 101\nWalnut Creek, CA 94596\nT: 925.736.9990 | F: 925.984.2621', align='Right')
        self.ln(4)
        self.set_margins(20,1,20)
        current_y = self.get_y()  # 5mm below the current text position
        start_x = self.l_margin  # Left margin
        end_x = self.w - self.r_margin  # Total page width minus right margin
        self.line(start_x, current_y, end_x, current_y)

        # 3. Move the cursor below the line before writing more text
        self.set_y(current_y + 5)

def get_attorney():
    response_attorney = True
    while response_attorney:
        response = input('Who is the Attorney? (Please only type in Jang, Amir, Daniel, or Sam)\n')

        if response.lower() == 'jang':
            response_attorney = False
            return('jang')
        elif response.lower() == 'amir':
            response_attorney = False
            return('amir')
        elif response.lower() == 'daniel':
            response_attorney = False
            return('daniel')
        elif response.lower() == 'sam':
            response_attorney = False
            return('sam')
        elif response.lower() == 'samual':
            response_attorney = False
            return('sam')
        else:
            pprint(f'You responded with {response}. Please only enter Jang, Amir, Daniel, or Sam.\n')

def get_case_manager():
    response_case_manager = True
    while response_case_manager:
        response = input('Who is the Case Manager?\n')

        if response.lower() == 'frank':
            response_case_manager = False
            return('frank')
        elif response.lower() == 'jeff':
            response_case_manager = False
            return('jeff')
        elif response.lower() == 'jennifer':
            response_case_manager = False
            return('jennifer')
        elif response.lower() == 'grace':
            response_case_manager = False
            return('grace')
        elif response.lower() == 'marla':
            response_case_manager = False
            return('marla')
        elif response.lower() == 'anabel':
            response_case_manager = False
            return('anabel')
        elif response.lower() == 'jacob':
            response_case_manager = False
            return('jacob')
        elif response.lower() == 'roman':
            response_case_manager = False
            return ('roman')
        else:
            pprint(f'You responded with {response}. Please only enter Frank, Jeff, Jennifer, Grace, Marla, Anabel, Jacob, or Roman.\n')


def get_signature(name):
    if name == 'jang':
        return('jang.jpg')
    elif name == 'amir':
        return('AG Signature.JPG')
    elif name == 'daniel':
        return('Daniel Signature.png')
    elif name == 'sam':
        return('Samual LC Dollar Signature.jpg')

attorney_dict = {
    'jang':'Jang Im',
    'sam':'Samual LC Dollar',
    'amir':'Amir Guedoir',
    'daniel':'Daniel Platt'
}

case_manager_dict = {
    'frank':{
        'name':'Frank Hur',
        'email':'frank@blackhawklawgroup.com',
        'phone_number':'(925) 475-5577 ext. 1014'
    },
    'jeff':{
        'name':'Jeff Oh',
        'email':'jeff@blackhawklawgroup.com',
        'phone_number':'(925) 744-5364'
        },
    'jennifer':{
        'name':'Jennifer Hernandez',
        'email':'jennifer@blackhawklawgroup.com',
        'phone_number':'(747) 244-6196'
        },
    'grace':{
        'name':'Grace Carpio',
        'email':'grace@blackhawklawgroup.com',
        'phone_number':'(925) 659-3901'
    },
    'marla':{
        'name':'Marla Benavides',
        'email':'marla@blackhawklawgroup.com',
        'phone_number':'(831) 334-2104'
        },
    'anabel':{
        'name':'Anabel Ramirez',
        'email':'anabel@blackhawklawgroup.com',
        'phone_number':'(925) 475-5551'
    },
    'roman':{
        'name':'Roman Gomez',
        'email':'roman@blackhawklawgroup.com',
        'phone_number':'(925) 752-5034'
    },
    'jacob':{
        'name':'Jacob Polk',
        'email':'jacob@blackhawklawgroup.com',
        'phone_number':'(707) 290-8551'
    },
}

def facility_letter(row):
    pdf = CustomPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.multi_cell(w=180, h=5,
                   text=f'{get_Today()}\n\n{row['Name of Recipient']}\n{row['Address 1 of Recipient']}\n{row['City of Recipient']}, {row['State of Recipient']} {row['Zip Code of Recipient']}',
                   align='L')
    pdf.ln(10)
    current_y = pdf.get_y()
    pdf.multi_cell(w=85, text='RE:       Client Name:', align='R')
    pdf.set_xy(105, current_y)
    pdf.multi_cell(w=85, text=f'{row['Client Name']}', align='L')
    pdf.ln(1)
    current_y = pdf.get_y()
    pdf.multi_cell(w=85, text='Date of Birth:', align='R')
    pdf.set_xy(105, current_y)
    pdf.multi_cell(w=85, text=f'{date_of_birth}', align='L')
    pdf.ln(1)
    current_y = pdf.get_y()
    pdf.multi_cell(w=85, text='Date of Loss:', align='R')
    pdf.set_xy(105, current_y)
    pdf.multi_cell(w=85, text=f'{date_of_loss}', align='L')
    pdf.ln(10)
    pdf.cell(text=f'Dear {row['Name of Recipient']}:')
    pdf.ln(8)
    pdf.multi_cell(w=170, h=5,
                   text=f'{INDENT}Enclosed please find check number {row['Check Number']} in the amount of ${row['Amount']:,.2f} as full payment of the above-referenced client\'s medical bill.')
    pdf.ln(5)
    pdf.multi_cell(w=170, h=5,
                   text=f'{INDENT}  Should you have any questions regarding this matter, please do not hesitate to contact our office.')
    pdf.ln(20)
    pdf.multi_cell(w=170, text='Very Truly Yours,', align="C")
    pdf.ln(5)
    pdf.set_x(80)

    pdf.image(name=resource_path(get_signature(attorney)), w=50, h=30)
    pdf.ln(5)
    pdf.multi_cell(w=170, h=5,
                   text=f'{attorney_dict[attorney]}\nAttorney at Law\n\n{case_manager_dict[case_manager]['name']}\nCase Manager\n{case_manager_dict[case_manager]['email']}\nTel: {case_manager_dict[case_manager]['phone_number']}',
                   align="C")

    pdf.output(f'Disbursement-{row['Client Name']}-{row['Name of Recipient']} - {row['Date of Loss'].strftime('%m.%d.%Y')}.pdf')

def client_letter(row):
    pdf = CustomPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.multi_cell(w=180, h=5,
               text=f'{get_Today()}\n\n{row['Client Name']}\n{row['Address 1 of Recipient']}\n{row['City of Recipient']}, {row['State of Recipient']} {row['Zip Code of Recipient']}',
               align='L')
    pdf.ln(10)
    current_y = pdf.get_y()
    pdf.multi_cell(w=170, text=f'RE:       Your Accident on {date_of_loss}:', align='C')
    pdf.ln(10)
    pdf.cell(text=f'Dear {row['Client Name']}:')
    pdf.ln(8)
    '''     
    pdf.multi_cell(w=170, h=5,
       text=f'{INDENT}As discussed in our phone call, we were able to get your Medi-Cal lien reduced. Enclosed please find check number {row['Check Number']} in the amount of ${row['Amount']:,.2f} for the difference.')
    '''
    pdf.multi_cell(w=170, h=5,
                   text=f'{INDENT}Enclosed please find check number {row['Check Number']} in the amount of ${row['Amount']:,.2f} as your full settlement proceeds from {row['Insurance']}.')
    pdf.ln(5)
    pdf.multi_cell(w=170, h=5,
                   text=f'{INDENT}  Thank you for allowing me the opportunity to represent you. If we may be of assistance in the future to you or anyone you know, we hope that you will contact us.')
    pdf.ln(20)
    pdf.multi_cell(w=170, text='Very Truly Yours,', align="C")
    pdf.ln(5)
    pdf.set_x(80)
    pdf.image(name=resource_path(get_signature(attorney)), w=50, h=30)
    pdf.ln(5)
    pdf.multi_cell(w=170, h=5,
                   text=f'{attorney_dict[attorney]}\nAttorney at Law\n\n{case_manager_dict[case_manager]['name']}\nCase Manager\n{case_manager_dict[case_manager]['email']}\nTel: {case_manager_dict[case_manager]['phone_number']}',
                   align="C")

    pdf.output(f'Disbursement-{row['Client Name']} - {row['Date of Loss'].strftime('%m.%d.%Y')}.pdf')

def combined_letter_client(row, pdf):
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.multi_cell(w=180, h=5,
                   text=f'{get_Today()}\n\n{row['Client Name']}\n{row['Address 1 of Recipient']}\n{row['City of Recipient']}, {row['State of Recipient']} {row['Zip Code of Recipient']}',
                   align='L')
    pdf.ln(10)
    current_y = pdf.get_y()
    pdf.multi_cell(w=170, text=f'RE:       Your Accident on {date_of_loss}:', align='C')
    pdf.ln(10)
    pdf.cell(text=f'Dear {row['Client Name']}:')
    pdf.ln(8)
    '''     
    pdf.multi_cell(w=170, h=5,
       text=f'{INDENT}As discussed in our phone call, we were able to get your Medi-Cal lien reduced. Enclosed please find check number {row['Check Number']} in the amount of ${row['Amount']:,.2f} for the difference.')
    '''
    pdf.multi_cell(w=170, h=5,
                   text=f'{INDENT}Enclosed please find check number {row['Check Number']} in the amount of ${row['Amount']:,.2f} as your full settlement proceeds from {row['Insurance']}.')
    pdf.ln(5)
    pdf.multi_cell(w=170, h=5,
                   text=f'{INDENT}  Thank you for allowing me the opportunity to represent you. If we may be of assistance in the future to you or anyone you know, we hope that you will contact us.')
    pdf.ln(20)
    pdf.multi_cell(w=170, text='Very Truly Yours,', align="C")
    pdf.ln(5)
    pdf.set_x(80)
    pdf.image(name=resource_path(get_signature(attorney)), w=50, h=30)
    pdf.ln(5)
    pdf.multi_cell(w=170, h=5,
                   text=f'{attorney_dict[attorney]}\nAttorney at Law\n\n{case_manager_dict[case_manager]['name']}\nCase Manager\n{case_manager_dict[case_manager]['email']}\nTel: {case_manager_dict[case_manager]['phone_number']}',
                   align="C")

def combined_letter_facility(row, pdf):
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.multi_cell(w=180, h=5,
                   text=f'{get_Today()}\n\n{row['Name of Recipient']}\n{row['Address 1 of Recipient']}\n{row['City of Recipient']}, {row['State of Recipient']} {row['Zip Code of Recipient']}',
                   align='L')
    pdf.ln(10)
    current_y = pdf.get_y()
    pdf.multi_cell(w=85, text='RE:       Client Name:', align='R')
    pdf.set_xy(105, current_y)
    pdf.multi_cell(w=85, text=f'{row['Client Name']}', align='L')
    pdf.ln(1)
    current_y = pdf.get_y()
    pdf.multi_cell(w=85, text='Date of Birth:', align='R')
    pdf.set_xy(105, current_y)
    pdf.multi_cell(w=85, text=f'{date_of_birth}', align='L')
    pdf.ln(1)
    current_y = pdf.get_y()
    pdf.multi_cell(w=85, text='Date of Loss:', align='R')
    pdf.set_xy(105, current_y)
    pdf.multi_cell(w=85, text=f'{date_of_loss}', align='L')
    pdf.ln(10)
    pdf.cell(text=f'Dear {row['Name of Recipient']}:')
    pdf.ln(8)
    pdf.multi_cell(w=170, h=5,
                   text=f'{INDENT}Enclosed please find check number {row['Check Number']} in the amount of ${row['Amount']:,.2f} as full payment of the above-referenced client\'s medical bill.')
    pdf.ln(5)
    pdf.multi_cell(w=170, h=5,
                   text=f'{INDENT}  Should you have any questions regarding this matter, please do not hesitate to contact our office.')
    pdf.ln(20)
    pdf.multi_cell(w=170, text='Very Truly Yours,', align="C")
    pdf.ln(5)
    pdf.set_x(80)

    pdf.image(name=resource_path(get_signature(attorney)), w=50, h=30)
    pdf.ln(5)
    pdf.multi_cell(w=170, h=5,
                   text=f'{attorney_dict[attorney]}\nAttorney at Law\n\n{case_manager_dict[case_manager]['name']}\nCase Manager\n{case_manager_dict[case_manager]['email']}\nTel: {case_manager_dict[case_manager]['phone_number']}',
                   align="C")

try:
    location = input('Please enter the file location\n')
    excelfile = pd.read_excel(f'{location}')
    attorney = get_attorney()
    case_manager = get_case_manager()
    pprint(excelfile)
    INDENT = ' ' * 8
    for index, row in excelfile.iterrows():
        date_of_birth = row['Date of Birth'].strftime('%m/%d/%Y')
        date_of_loss = row['Date of Loss'].strftime('%m/%d/%Y')
        pprint(f'{index}: {row['Client Name']}, {row['Date of Loss']}, {row['Date of Birth']}')
        if row['Name of Recipient'] != 'CLIENT':
            facility_letter(row)
        else:
            client_letter(row)
    pdf = CustomPDF()
    for index, row in excelfile.iterrows():

        date_of_birth = row['Date of Birth'].strftime('%m/%d/%Y')
        date_of_loss = row['Date of Loss'].strftime('%m/%d/%Y')
        pprint(f'{index}: {row['Client Name']}, {row['Date of Loss']}, {row['Date of Birth']}')
        if row['Name of Recipient'] != 'CLIENT':
            combined_letter_facility(row, pdf)
        else:
            combined_letter_client(row, pdf)
    pdf.output(f'Disbursement-Combined-{get_Today()}.pdf')

except Exception as e:
    pprint('error')
    with open("error_log.txt", "w") as file:
        traceback.print_exc(file=file)

#C:\Users\Alvin\Downloads\DisbursementTemplate.xlsx