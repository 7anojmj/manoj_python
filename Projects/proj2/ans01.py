import csv
import os
import re
from fpdf import FPDF
from datetime import date
from datetime import datetime

directory = os.getcwd()
destination_folder = 'transcriptsIITP'
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

destination = os.path.join(os.getcwd(), "transcriptsIITP")


# source =os.path.join(os.getcwd(),"wrong_srt")
# temp = os.path.join(os.getcwd(),"temp_srt")
invalid_list = []

def creator(data,stamp,sign):
    os.chdir(directory)
    # print('in creator now')
    stu_details = data[0][0]
    sroll = stu_details[0]
    sname = stu_details[1]
    syear = stu_details[2]
    sbranch = stu_details[3]
    filename = sroll+'.pdf'

    sem1_details = data[0][1][0]
    sem1_summary = data[0][1][1]

    sem2_details = data[0][2][0]
    sem2_summary = data[0][2][1]

    sem3_details = data[0][3][0]
    sem3_summary = data[0][3][1]

    sem4_details = data[0][4][0]
    sem4_summary = data[0][4][1]

    sem5_details = data[0][5][0]
    sem5_summary = data[0][5][1]

    sem6_details = data[0][6][0]
    sem6_summary = data[0][6][1]

    sem7_details = data[0][7][0]
    sem7_summary = data[0][7][1]

    sem8_details = data[0][8][0]
    sem8_summary = data[0][8][1]

    # print(sem8_details)
    # print(sem8_summary)

    '''-------------------------added here-----------------------'''


    # print(sem8_details)
    # print(sem8_summary)

    fpdf = FPDF(orientation='L', unit='mm', format='A3')
    fpdf.add_page()
    x = fpdf.get_x()
    y = fpdf.get_y()
    fpdf.set_font("Arial", size=8)
    # print(x,y)
    fpdf.image('tlogo2.png', x=12, y=12, w=400, h=27, type='', link='')
    # fpdf.line(0,30,40,30)
    fpdf.set_line_width(width=0.5)
    fpdf.line(14, 38, 14, 285)    # left margin
    fpdf.line(409, 38, 409, 285)  # right margin
    fpdf.line(14, 285, 409, 285)  # bottom margin

    # fpdf.set_x(x=70)
    # fpdf.set_y(y=50)
    fpdf.set_line_width(width=0.1)
    line_height = (fpdf.font_size * 2.5) - 2
    '''--------------------student details------------------------------------------'''

    fpdf.set_xy(x=110, y=43)
    fpdf.multi_cell(w=15, h=line_height, txt='Roll No :', border=0, align='L')
    fpdf.set_xy(x=123, y=43)
    fpdf.multi_cell(w=17, h=line_height, txt=sroll, border=1, align='C')
    fpdf.set_xy(x=153, y=43)
    fpdf.multi_cell(w=16, h=line_height, txt='Name', border=0, align='L')
    fpdf.set_xy(x=163, y=43)
    fpdf.multi_cell(w=100, h=line_height, txt=sname, border=1, align='C')
    fpdf.set_xy(x=273, y=43)
    fpdf.multi_cell(w=40, h=line_height, txt='Year of Admission :', border=0, align='L')
    fpdf.set_xy(x=300, y=43)
    fpdf.multi_cell(w=10, h=line_height, txt=syear, border=1, align='C')

    fpdf.set_xy(x=110, y=50)
    fpdf.multi_cell(w=18, h=line_height, txt='Programme :', border=0, align='L')
    fpdf.set_xy(x=128, y=50)
    fpdf.multi_cell(w=35, h=line_height, txt='Bachelor Of Technology', border=1, align='C')
    fpdf.set_xy(x=210, y=50)
    fpdf.multi_cell(w=16, h=line_height, txt='Course : ', border=0, align='L')
    fpdf.set_xy(x=225, y=50)
    fpdf.multi_cell(w=60, h=line_height, txt=sbranch, border=1, align='C')

    fpdf.set_line_width(width=0.4)
    fpdf.rect(x=105, y=42, w=210, h=16, style='')

    fpdf.line(14, 203, 409, 203)  # 2/3 rd  margin
    fpdf.line(14, 126, 409, 126)  # 1/3 rd  margin

    fpdf.set_line_width(width=0.05)
    off_x = 20
    off_y = 65
    '''-------------------sem 1 ----------------------------------'''
    if sem1_details:
        fpdf.set_xy(x=20, y=60)
        fpdf.set_font("Arial", 'B', size=8)
        fpdf.multi_cell(w=60, h=line_height, txt='Semester 1 ', border=0, align='L')
        fpdf.set_font("Arial", size=8)
        fpdf.set_xy(x=off_x, y=off_y)
        # line_height = fpdf.font_size * 2.5
        col_width = 10
        for row in sem1_details:
            i = 0
            fpdf.set_xy(x=off_x, y=off_y)
            for datum in row:
                if i == 1:
                    cwidth = 50
                    fpdf.cell(65, line_height, datum, border=1, ln=0)
                    i = i + 1
                else:
                    fpdf.cell(13, line_height, datum, border=1, ln=0)
                    i = i + 1
            fpdf.ln(line_height)
            # off_x=off_x+line_height
            off_y = off_y + line_height

        fpdf.set_xy(x=20, y=115)
        i = 0
        for item in sem1_summary:

            if i == 0 or i == 2:
                fpdf.cell(22, line_height, item, border=0, ln=0)
                i = i + 1
            else:
                fpdf.cell(9, line_height, item, border=0, ln=0)
                i = i + 1

        fpdf.set_line_width(width=0.4)
        fpdf.rect(x=20, y=115, w=105, h=7, style='')

    fpdf.set_line_width(width=0.05)

    '''--------------------------sem 2-------------------------------------------'''
    off_x = 150
    off_y = 65

    if sem2_details:
        fpdf.set_xy(x=150, y=60)
        fpdf.set_font("Arial", 'B', size=8)
        fpdf.multi_cell(w=60, h=line_height, txt='Semester 2 ', border=0, align='L')
        fpdf.set_font("Arial", size=8)

        fpdf.set_xy(x=off_x, y=off_y)
        # line_height = fpdf.font_size * 2.5
        col_width = 10
        for row in sem2_details:
            i = 0
            fpdf.set_xy(x=off_x, y=off_y)
            for datum in row:
                if i == 1:
                    cwidth = 50
                    fpdf.cell(65, line_height, datum, border=1, ln=0)
                    i = i + 1
                else:
                    fpdf.cell(13, line_height, datum, border=1, ln=0)
                    i = i + 1
            fpdf.ln(line_height)
            # off_x=off_x+line_height
            off_y = off_y + line_height

        fpdf.set_xy(x=150, y=115)
        i = 0
        for item in sem2_summary:

            if i == 0 or i == 2:
                fpdf.cell(22, line_height, item, border=0, ln=0)
                i = i + 1
            else:
                fpdf.cell(9, line_height, item, border=0, ln=0)
                i = i + 1

        fpdf.set_line_width(width=0.4)
        fpdf.rect(x=150, y=115, w=105, h=7, style='')

    fpdf.set_line_width(width=0.05)

    '''----------------------------------------------------------------------'''

    '''-----------------------------sem 3----------------------------------------'''
    off_x = 280
    off_y = 65
    if sem3_details:
        fpdf.set_xy(x=280, y=60)
        fpdf.set_font("Arial", 'B', size=8)
        fpdf.multi_cell(w=60, h=line_height, txt='Semester 3 ', border=0, align='L')
        fpdf.set_font("Arial", size=8)

        fpdf.set_xy(x=off_x, y=off_y)
        # line_height = fpdf.font_size * 2.5
        col_width = 10
        for row in sem3_details:
            i = 0
            fpdf.set_xy(x=off_x, y=off_y)
            for datum in row:
                if i == 1:
                    cwidth = 50
                    fpdf.cell(65, line_height, datum, border=1, ln=0)
                    i = i + 1
                else:
                    fpdf.cell(13, line_height, datum, border=1, ln=0)
                    i = i + 1
            fpdf.ln(line_height)
            # off_x=off_x+line_height
            off_y = off_y + line_height

        fpdf.set_xy(x=280, y=115)
        i = 0
        for item in sem3_summary:

            if i == 0 or i == 2:
                fpdf.cell(22, line_height, item, border=0, ln=0)
                i = i + 1
            else:
                fpdf.cell(9, line_height, item, border=0, ln=0)
                i = i + 1

        fpdf.set_line_width(width=0.4)
        fpdf.rect(x=280, y=115, w=105, h=7, style='')

    fpdf.set_line_width(width=0.05)

    '''------------------------------sem 4---------------------------------------'''
    off_x = 20
    off_y = 135
    if sem4_details:
        fpdf.set_xy(x=20, y=130)
        fpdf.set_font("Arial", 'B', size=8)
        fpdf.multi_cell(w=60, h=line_height, txt='Semester 4 ', border=0, align='L')
        fpdf.set_font("Arial", size=8)

        fpdf.set_xy(x=off_x, y=off_y)
        # line_height = fpdf.font_size * 2.5
        col_width = 10
        for row in sem4_details:
            i = 0
            fpdf.set_xy(x=off_x, y=off_y)
            for datum in row:
                if i == 1:
                    cwidth = 50
                    fpdf.cell(65, line_height, datum, border=1, ln=0)
                    i = i + 1
                else:
                    fpdf.cell(13, line_height, datum, border=1, ln=0)
                    i = i + 1
            fpdf.ln(line_height)
            # off_x=off_x+line_height
            off_y = off_y + line_height

        fpdf.set_xy(x=20, y=188)
        i = 0
        for item in sem4_summary:

            if i == 0 or i == 2:
                fpdf.cell(22, line_height, item, border=0, ln=0)
                i = i + 1
            else:
                fpdf.cell(9, line_height, item, border=0, ln=0)
                i = i + 1

        fpdf.set_line_width(width=0.4)
        fpdf.rect(x=20, y=188, w=105, h=7, style='')

    fpdf.set_line_width(width=0.05)

    '''-----------------------------sem 5----------------------------------------'''
    off_x = 150
    off_y = 135

    if sem5_details:
        fpdf.set_xy(x=150, y=130)
        fpdf.set_font("Arial", 'B', size=8)
        fpdf.multi_cell(w=60, h=line_height, txt='Semester 5 ', border=0, align='L')
        fpdf.set_font("Arial", size=8)
        fpdf.set_xy(x=off_x, y=off_y)
        # line_height = fpdf.font_size * 2.5
        col_width = 10
        for row in sem5_details:
            i = 0
            fpdf.set_xy(x=off_x, y=off_y)
            for datum in row:
                if i == 1:
                    cwidth = 50
                    fpdf.cell(65, line_height, datum, border=1, ln=0)
                    i = i + 1
                else:
                    fpdf.cell(13, line_height, datum, border=1, ln=0)
                    i = i + 1
            fpdf.ln(line_height)
            # off_x=off_x+line_height
            off_y = off_y + line_height

        fpdf.set_xy(x=150, y=188)
        i = 0
        for item in sem5_summary:

            if i == 0 or i == 2:
                fpdf.cell(22, line_height, item, border=0, ln=0)
                i = i + 1
            else:
                fpdf.cell(9, line_height, item, border=0, ln=0)
                i = i + 1

        fpdf.set_line_width(width=0.4)
        fpdf.rect(x=150, y=188, w=105, h=7, style='')

    fpdf.set_line_width(width=0.05)

    '''-----------------------------sem 6----------------------------------------'''
    off_x = 280
    off_y = 135
    if sem6_details:
        fpdf.set_xy(x=280, y=130)
        fpdf.set_font("Arial", 'B', size=8)
        fpdf.multi_cell(w=60, h=line_height, txt='Semester 6 ', border=0, align='L')
        fpdf.set_font("Arial", size=8)
        fpdf.set_xy(x=off_x, y=off_y)
        # line_height = fpdf.font_size * 2.5
        col_width = 10
        for row in sem6_details:
            i = 0
            fpdf.set_xy(x=off_x, y=off_y)
            for datum in row:
                if i == 1:
                    cwidth = 50
                    fpdf.cell(65, line_height, datum, border=1, ln=0)
                    i = i + 1
                else:
                    fpdf.cell(13, line_height, datum, border=1, ln=0)
                    i = i + 1
            fpdf.ln(line_height)
            # off_x=off_x+line_height
            off_y = off_y + line_height

        fpdf.set_xy(x=280, y=188)
        i = 0
        for item in sem6_summary:

            if i == 0 or i == 2:
                fpdf.cell(22, line_height, item, border=0, ln=0)
                i = i + 1
            else:
                fpdf.cell(9, line_height, item, border=0, ln=0)
                i = i + 1

        fpdf.set_line_width(width=0.4)
        fpdf.rect(x=280, y=187, w=105, h=7, style='')

    fpdf.set_line_width(width=0.05)

    '''------------------------------sem 7---------------------------------------'''
    off_x = 20
    off_y = 215
    if sem7_details:
        fpdf.set_xy(x=20, y=210)
        fpdf.set_font("Arial", 'B', size=8)
        fpdf.multi_cell(w=60, h=line_height, txt='Semester 7 ', border=0, align='L')
        fpdf.set_font("Arial", size=8)
        fpdf.set_xy(x=off_x, y=off_y)
        # line_height = fpdf.font_size * 2.5
        col_width = 10
        for row in sem7_details:
            i = 0
            fpdf.set_xy(x=off_x, y=off_y)
            for datum in row:
                if i == 1:
                    cwidth = 50
                    fpdf.cell(65, line_height, datum, border=1, ln=0)
                    i = i + 1
                else:
                    fpdf.cell(13, line_height, datum, border=1, ln=0)
                    i = i + 1
            fpdf.ln(line_height)
            # off_x=off_x+line_height
            off_y = off_y + line_height

        fpdf.set_xy(x=20, y=265)
        i = 0
        for item in sem7_summary:

            if i == 0 or i == 2:
                fpdf.cell(22, line_height, item, border=0, ln=0)
                i = i + 1
            else:
                fpdf.cell(9, line_height, item, border=0, ln=0)
                i = i + 1

        fpdf.set_line_width(width=0.4)
        fpdf.rect(x=20, y=265, w=105, h=7, style='')

    fpdf.set_line_width(width=0.05)

    '''------------------------------sem 8 ---------------------------------------'''
    off_x = 150
    off_y = 215
    if sem8_details:
        fpdf.set_xy(x=150, y=210)
        fpdf.set_font("Arial", 'B', size=8)
        fpdf.multi_cell(w=60, h=line_height, txt='Semester 8 ', border=0, align='L')
        fpdf.set_font("Arial", size=8)
        fpdf.set_xy(x=off_x, y=off_y)
        # line_height = fpdf.font_size * 2.5
        col_width = 10
        for row in sem8_details:
            i = 0
            fpdf.set_xy(x=off_x, y=off_y)
            for datum in row:
                if i == 1:
                    cwidth = 50
                    fpdf.cell(65, line_height, datum, border=1, ln=0)
                    i = i + 1
                else:
                    fpdf.cell(13, line_height, datum, border=1, ln=0)
                    i = i + 1
            fpdf.ln(line_height)
            # off_x=off_x+line_height
            off_y = off_y + line_height

        fpdf.set_xy(x=150, y=265)
        i = 0
        for item in sem8_summary:

            if i == 0 or i == 2:
                fpdf.cell(22, line_height, item, border=0, ln=0)
                i = i + 1
            else:
                fpdf.cell(9, line_height, item, border=0, ln=0)
                i = i + 1

        fpdf.set_line_width(width=0.4)
        fpdf.rect(x=150, y=265, w=105, h=7, style='')

    fpdf.set_line_width(width=0.05)

    '''----------------------------------------------------------------------'''
    fpdf.set_font("Arial", 'B', size=12)
    fpdf.set_xy(x=280, y=210)
    fpdf.multi_cell(w=100, h=line_height, txt='Date Generated : ', border=0, align='C')

    now = datetime.now()
    today = date.today()

    day = today.strftime("%d %b %Y")
    current_time = now.strftime('%H : %M ')
    dt = str(day) + " , " + str(current_time)
    # print(dt)

    fpdf.set_xy(x=300, y=210)
    fpdf.multi_cell(w=100, h=line_height, txt=dt, border=0, align='R')

    fpdf.set_xy(x=311, y=255)
    fpdf.multi_cell(w=100, h=line_height, txt='________________________________', border=0, align='C')

    fpdf.set_xy(x=327, y=260)
    fpdf.multi_cell(w=100, h=line_height, txt='Assistant Registrator (Academic)', border=0, align='L')
    os.chdir(directory)
    if len(os.listdir('stamp_dir'))>0 :
        fpdf.image(stamp, x=270, y=220, w=50, h=40, type='', link='')

    if len(os.listdir('sign_dir'))>0:
        fpdf.image(sign, x=350, y=235, w=20, h=15, type='', link='')

    # fpdf.rect(x: float, y: float, w: float, h: float, style = '')
    # fpdf.rect(x=110, y=50, w=60, h= 50, style = '')
    os.chdir(destination)
    fpdf.output(filename,'F')
    print('Transcript generated for rollno :',sroll)


def looper (com_roll_data,inp_rlis,stamp,sign):
    print('generating pdfs...')
    global invalid_list
    for i in inp_rlis:
        if i in com_roll_data.keys():
            # print(com_roll_data[i])
            creator(com_roll_data[i],stamp,sign)
        else:
            invalid_list.append(i)

    if invalid_list:
        print(invalid_list , 'these roll numbers doesnot exhist')
    # print('invalid list is',invalid_list)

    return




def generate_sem_data(inp_rlis, stamp, sign):
    grade = {'AA': 10,
             'AB': 9,
             'BB': 8,
             ' BB': 8,
             'BC': 7,
             'CC': 6,
             'CD': 5,
             'DD': 4,
             'DD*': 4,
             'F*': 0,
             'F': 0,
             'I': 0
             }

    branch = {'ME': 'MECHANICAL ENGINEERING',
              'CS': 'COMPUTER SCIENCE AND ENGINEERING',
              'CB': 'CHEMICAL ENGINEERING',
              'CE': 'CIVIL ENGINEERING',
              'MM': 'METULLERGICAL ENGINEERING',
              'EE': 'ELECTRICAL ENGINEERING',
              }

    # print('in generate sem data lopp',os.getcwd())
    print('generating data...')
    # source = os.path.join(os.getcwd())
    source = os.path.join(os.getcwd(), "sample_input")
    destination = os.path.join(os.getcwd(), "transcriptsIITP")
    output = os.path.join(os.getcwd(), 'output')
    # try:
    #     os.makedirs(destination)
    # except:
    #     pass

    os.chdir(source)

    com_roll_data = {}

    with open('names-roll.csv', 'r') as f1:
        reader1 = csv.reader(f1)
        next(reader1)
        for x in reader1:

            rno = str(x[0])

            rl = re.split('(\d+)', rno)
            rl.pop(0)
            rl.pop(-1)
            rl[1] = rl[1].upper()
            bran = branch[rl[1]]
            rno = rl[0] + rl[1] + rl[2]

            name = str(x[1])
            year = str(20) + str(rno[:2])

            # print(rno,name,year)
            head = ['Sub Code', 'Subject Name', 'L-T-P', 'CRD', 'GRD']

            semdata1 = []
            semdata2 = []
            semdata3 = []
            semdata4 = []
            semdata5 = []
            semdata6 = []
            semdata7 = []
            semdata8 = []
            semdata1.append(head)
            semdata2.append(head)
            semdata3.append(head)
            semdata4.append(head)
            semdata5.append(head)
            semdata6.append(head)
            semdata7.append(head)
            semdata8.append(head)
            # print(semdata1)

            with open('grades.csv', 'r') as f2:
                reader2 = csv.reader(f2)
                next(reader2)
                s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = 1
                c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = 0
                sp1 = sp2 = sp3 = sp4 = sp5 = sp6 = sp7 = sp8 = 0
                tc1 = tc2 = tc3 = tc4 = tc5 = tc6 = tc7 = tc8 = 0
                cp1 = cp2 = cp3 = cp4 = cp5 = cp6 = cp7 = cp8 = 0
                cc1 = cc2 = cc3 = cc4 = cc5 = cc6 = cc7 = cc8 = 0
                for i in reader2:
                    if i[1] == '1' and i[0] == rno:
                        with open('subjects_master.csv', 'r') as f3:
                            reader3 = csv.reader(f3)
                            next(reader3)
                            for j in reader3:
                                if i[2] == j[0]:
                                    data = [i[2], j[1], j[2], i[3], i[4]]
                                    '''-----------------------'''
                                    credit_obtaied = int(grade[i[4]])

                                    if credit_obtaied != 0:
                                        cc1 = cc1 + int(i[3])

                                    '''------------------------'''
                                    c1 = c1 + int(i[3])
                                    s1 = s1 + 1
                                    sp1 = sp1 + (int(i[3]) * int(grade[i[4]]))
                                    # print(int(grade[i[4]]))

                                    semdata1.append(data)
                                tc1 = c1
                            # print('data is -------------',data)


                    elif i[1] == '2' and i[0] == rno:
                        with open('subjects_master.csv', 'r') as f3:
                            reader3 = csv.reader(f3)
                            next(reader3)
                            for j in reader3:
                                if i[2] == j[0]:
                                    data = [i[2], j[1], j[2], i[3], i[4]]
                                    '''-----------------------'''
                                    credit_obtaied = int(grade[i[4]])

                                    if credit_obtaied != 0:
                                        cc2 = cc2 + int(i[3])

                                    '''------------------------'''
                                    c2 = c2 + int(i[3])
                                    sp2 = sp2 + (int(i[3]) * int(grade[i[4]]))
                                    s2 = s2 + 1

                                    semdata2.append(data)
                                tc2 = tc1 + c2

                    elif i[1] == '3' and i[0] == rno:
                        with open('subjects_master.csv', 'r') as f3:
                            reader3 = csv.reader(f3)
                            next(reader3)
                            for j in reader3:
                                if i[2] == j[0]:
                                    data = [i[2], j[1], j[2], i[3], i[4]]
                                    '''-----------------------'''
                                    credit_obtaied = int(grade[i[4]])

                                    if credit_obtaied != 0:
                                        cc3 = cc3 + int(i[3])

                                    '''------------------------'''
                                    c3 = c3 + int(i[3])
                                    sp3 = sp3 + (int(i[3]) * int(grade[i[4]]))
                                    s3 = s3 + 1

                                    semdata3.append(data)
                                tc3 = tc2 + c3

                    elif i[1] == '4' and i[0] == rno:
                        with open('subjects_master.csv', 'r') as f3:
                            reader3 = csv.reader(f3)
                            next(reader3)
                            for j in reader3:
                                if i[2] == j[0]:
                                    data = [i[2], j[1], j[2], i[3], i[4]]
                                    '''-----------------------'''
                                    credit_obtaied = int(grade[i[4]])

                                    if credit_obtaied != 0:
                                        cc4 = cc4 + int(i[3])

                                    '''------------------------'''
                                    c4 = c4 + int(i[3])
                                    sp4 = sp4 + (int(i[3]) * int(grade[i[4]]))
                                    s4 = s4 + 1

                                    semdata4.append(data)
                                tc4 = tc3 + c4

                    elif i[1] == '5' and i[0] == rno:
                        with open('subjects_master.csv', 'r') as f3:
                            reader3 = csv.reader(f3)
                            next(reader3)
                            for j in reader3:
                                if i[2] == j[0]:
                                    data = [i[2], j[1], j[2], i[3], i[4]]
                                    '''-----------------------'''
                                    credit_obtaied = int(grade[i[4]])

                                    if credit_obtaied != 0:
                                        cc5 = cc5 + int(i[3])

                                    '''------------------------'''
                                    c5 = c5 + int(i[3])
                                    sp5 = sp5 + (int(i[3]) * int(grade[i[4]]))
                                    s5 = s5 + 1

                                    semdata5.append(data)
                                tc5 = tc4 + c5

                    elif i[1] == '6' and i[0] == rno:
                        with open('subjects_master.csv', 'r') as f3:
                            reader3 = csv.reader(f3)
                            next(reader3)
                            for j in reader3:
                                if i[2] == j[0]:
                                    data = [i[2], j[1], j[2], i[3], i[4]]
                                    '''-----------------------'''
                                    credit_obtaied = int(grade[i[4]])

                                    if credit_obtaied != 0:
                                        cc6 = cc6 + int(i[3])

                                    '''------------------------'''
                                    c6 = c6 + int(i[3])
                                    sp6 = sp6 + (int(i[3]) * int(grade[i[4]]))
                                    s6 = s6 + 1

                                    semdata6.append(data)
                                tc6 = tc5 + c6

                    elif i[1] == '7' and i[0] == rno:
                        with open('subjects_master.csv', 'r') as f3:
                            reader3 = csv.reader(f3)
                            next(reader3)
                            for j in reader3:
                                if i[2] == j[0]:
                                    data = [i[2], j[1], j[2], i[3], i[4]]
                                    '''-----------------------'''
                                    credit_obtaied = int(grade[i[4]])

                                    if credit_obtaied != 0:
                                        cc7 = cc7 + int(i[3])

                                    '''------------------------'''
                                    c7 = c7 + int(i[3])
                                    sp7 = sp7 + (int(i[3]) * int(grade[i[4]]))
                                    s7 = s7 + 1

                                    semdata7.append(data)
                                tc7 = tc6 + c7

                    elif i[1] == '8' and i[0] == rno:
                        with open('subjects_master.csv', 'r') as f3:
                            reader3 = csv.reader(f3)
                            next(reader3)
                            for j in reader3:
                                if i[2] == j[0]:
                                    data = [i[2], j[1], j[2], i[3], i[4]]
                                    '''-----------------------'''
                                    credit_obtaied = int(grade[i[4]])

                                    if credit_obtaied != 0:
                                        cc8 = cc8 + int(i[3])

                                    '''------------------------'''
                                    c8 = c8 + int(i[3])
                                    sp8 = sp8 + (int(i[3]) * int(grade[i[4]]))
                                    s8 = s8 + 1

                                    semdata8.append(data)
                                tc8 = tc7 + c8

            sp1 = round(sp1 / c1, 2)
            sp2 = round(sp2 / c2, 2)
            if (c3):
                sp3 = round(sp3 / c3, 2)
            if (c4):
                sp4 = round(sp4 / c4, 2)
            if (c5):
                sp5 = round(sp5 / c5, 2)
            if (c6):
                sp6 = round(sp6 / c6, 2)
            if (c7):
                sp7 = round(sp7 / c7, 2)
            if (c8):
                sp8 = round(sp8 / c8, 2)
            cp1 = sp1
            cp2 = ((cp1 * tc1) + (sp2 * c2)) / tc2
            if (c3):
                cp3 = ((cp2 * tc2) + (sp3 * c3)) / tc3
            if (c4):
                cp4 = ((cp3 * tc3) + (sp4 * c4)) / tc4
            if (c5):
                cp5 = ((cp4 * tc4) + (sp5 * c5)) / tc5
            if (c6):
                cp6 = ((cp5 * tc5) + (sp6 * c6)) / tc6
            if (c7):
                cp7 = ((cp6 * tc6) + (sp7 * c7)) / tc7
            if (c8):
                cp8 = ((cp7 * tc7) + (sp8 * c8)) / tc8

            cp1 = round(cp1, 2)
            cp2 = round(cp2, 2)
            cp3 = round(cp3, 2)
            cp4 = round(cp4, 2)
            cp5 = round(cp5, 2)
            cp6 = round(cp6, 2)
            cp7 = round(cp7, 2)
            cp8 = round(cp8, 2)

            semdata1_ov = ['Credits Taken : ', str(c1), 'Credits Cleared : ', str(cc1), '  SPI : ', str(sp1),
                           '  CPI : ', str(cp1)]
            semdata2_ov = ['Credits Taken : ', str(c2), 'Credits Cleared : ', str(cc2), '  SPI : ', str(sp2),
                           '  CPI : ', str(cp2)]
            semdata3_ov = ['Credits Taken : ', str(c3), 'Credits Cleared : ', str(cc3), '  SPI : ', str(sp3),
                           '  CPI : ', str(cp3)]
            semdata4_ov = ['Credits Taken : ', str(c4), 'Credits Cleared : ', str(cc4), '  SPI : ', str(sp4),
                           '  CPI : ', str(cp4)]
            semdata5_ov = ['Credits Taken : ', str(c5), 'Credits Cleared : ', str(cc5), '  SPI : ', str(sp5),
                           '  CPI : ', str(cp5)]
            semdata6_ov = ['Credits Taken : ', str(c6), 'Credits Cleared : ', str(cc6), '  SPI : ', str(sp6),
                           '  CPI : ', str(cp6)]
            semdata7_ov = ['Credits Taken : ', str(c7), 'Credits Cleared : ', str(cc7), '  SPI : ', str(sp7),
                           '  CPI : ', str(cp7)]
            semdata8_ov = ['Credits Taken : ', str(c8), 'Credits Cleared : ', str(cc8), '  SPI : ', str(sp8),
                           '  CPI : ', str(cp8)]

            rollno = rno
            '''------------------'''
            s_info = [rollno, name, year, bran]
            com_sem1 = [semdata1, semdata1_ov]
            com_sem2 = [semdata2, semdata2_ov]
            com_sem3 = [semdata3, semdata3_ov]
            com_sem4 = [semdata4, semdata4_ov]
            com_sem5 = [semdata5, semdata5_ov]
            com_sem6 = [semdata6, semdata6_ov]
            com_sem7 = [semdata7, semdata7_ov]
            com_sem8 = [semdata8, semdata8_ov]

            if rollno not in com_roll_data:
                com_roll_data[rollno] = []
            com_roll_data[rollno].append(
                [s_info, com_sem1, com_sem2, com_sem3, com_sem4, com_sem5, com_sem6, com_sem7, com_sem8])

        looper(com_roll_data,inp_rlis,stamp,sign)


def list_generation(ran, stamp, sign):
    # ran = ' 0401CS01 - 0401CS02 '
    ran = ran.split('-')
    ran_lis = []
    for i in ran:
        i = i.replace(' ', '')
        ran_lis.append(i)
    print(ran_lis)

    '''----------------initial roll number ---------------------'''
    first_lis = re.split('(\d+)', ran_lis[0])
    first_lis.pop(0)
    first_lis.pop(-1)
    # print(first_lis)
    roll_start = int(first_lis[-1])
    # print(roll_start)
    br1 = first_lis[1].upper()
    # print(br1,type(br1))
    y1 = first_lis[0]
    # print(y1)

    '''--------------------ending roll number ----------------------'''
    sec_lis = re.split('(\d+)', ran_lis[1])
    sec_lis.pop(0)
    sec_lis.pop(-1)
    # print(sec_lis)
    roll_end = int(sec_lis[-1])
    # print(roll_end)
    br2 = sec_lis[1].upper()
    # print(br2,type(br2))
    y2 = sec_lis[0]
    # print(y2)

    '''-------------------------generating required list-------------------'''
    inp_rlis = []
    if y1==y2 and br1==br2 and roll_start==roll_end:
        if roll_start <10 :
            rollno = y1+br1+'0'+str(roll_start)
        else :
            rollno = y1+br1+str(roll_start)
        inp_rlis.append(rollno)
        generate_sem_data(inp_rlis, stamp, sign)
    elif y1==y2 and br1==br2 and roll_start!=roll_end:
        for i in range(roll_start,roll_end+1):
            if i < 10:
                rollno =y1+br1+'0'+str(i)
            else:
                rollno = y1+br1+str(i)
            inp_rlis.append(rollno)
        generate_sem_data(inp_rlis, stamp, sign)
    else :
        return "Invalid input given ,please try again"
        # print('Invalid input given')
        # exit()

    # generate_sem_data(inp_rlis,stamp,sign)


# list_generation('0401cs01-  0401cs04','ok','ok')
