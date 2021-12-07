#1901ME39
#MANOJ KUMAR MADUGULA


import csv
import os
from openpyxl import Workbook
# from openpyxl import Workbook
# import time


def output_by_subject():
    # print(data)
    # folder_name = "test00_sub_xl_tp"
    folder_name = "output_by_subject"
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    dict_subdata = {}
    with open('regtable_old.csv', mode='r') as f:
        data = csv.reader(f)
        for row in data:
            # roll = row[0]
            rollno = row[0]
            register_sem = row[1]
            subno = row[3]
            sub_type = row[-1]
            if subno not in dict_subdata:
                dict_subdata[subno] = []
                dict_subdata[subno].append(('rollno', 'register_sem', 'subno', 'sub_type'))
            dict_subdata[subno].append((rollno, register_sem, subno, sub_type))
            # print('in the looooooooooooooooop')
            # print(dict_rolldata, type(dict_rolldata))
        # print('ok-roll-2')

    for subno in dict_subdata:
        fdata = dict_subdata[subno]
        file_name = os.path.join(folder_name, subno + ".xlsx")
        # print(fdata)
        wb = Workbook()
        sheet = wb.active
        for i in fdata:
            sheet.append(i)
        wb.save(file_name)

    return

def output_individual_roll():
    # print(data)
    # print('ok-roll')
    dict_rolldata = {}
    # folder_name = "tut00_roll_xl_tp"
    folder_name = "output_individual_roll"
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


    with open('regtable_old.csv', mode='r') as f:
        data = csv.reader(f)

        for row in data:
            # roll = row[0]
            rollno = row[0]
            register_sem = row[1]
            subno = row[3]
            sub_type = row[-1]
            if rollno not in dict_rolldata:
                dict_rolldata[rollno] = []
                dict_rolldata[rollno].append(('rollno', 'register_sem', 'subno', 'sub_type'))
            dict_rolldata[rollno].append((rollno, register_sem, subno, sub_type))
            # print('in the looooooooooooooooop')
            # print(dict_rolldata, type(dict_rolldata))
        # print('ok-roll-2')



    for rollno in dict_rolldata:
        fdata= dict_rolldata[rollno]
        file_name = os.path.join(folder_name, rollno + ".xlsx")
        # print(fdata)
        wb = Workbook()
        sheet= wb.active
        for i in fdata:
            sheet.append(i)
        wb.save(file_name)


        # print(fdata[0])

    # print('ok-roll-3')
    
    return

output_by_subject()
output_individual_roll()