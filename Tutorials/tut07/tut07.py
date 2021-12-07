
# Manoj Kumar Madugula
# 1901ME39

import csv
import pandas as pd

output_file_name = "course_feedback_remaining.xlsx" 
'''------------------------------------------------------------------------------'''
course_master_data ={}
course_master_file = open('course_master_dont_open_in_excel.csv',mode='r')
course_master_reader = csv.DictReader(course_master_file)
cm_data_list = []
for row in course_master_reader:
    # print(row)
    raw = row['ltp']
    raw = raw.split('-')
    raw = [ float(i) for i in raw ]        
    # print(raw)
    nbits = 0 
    for i in raw :
        if i > 0:
            nbits=nbits+1
    # print(nbits)
    # course_master_data [row['subno']] = nbits
    course_master_data={ 
                        'subno'  : row['subno'],
                        # 'ltp'    : row['ltp'],
                        # 'l': raw[0],
                        # 't': raw[1],
                        # 'p': raw[2],
                        'non_zero_bits':nbits,   
                        }
    cm_data_list.append(course_master_data)
    
# print(course_master_data)
# print(course_master_data['CE111'])
course_master_data_df = pd.DataFrame(cm_data_list)
# course_master_data_df

''' ----------------------------------------------------------------------------------------- '''
studentinfo_data = { }
roll_in_studentinfo = []
studentinfo_list =[]
studentinfo_file = open('studentinfo.csv',mode='r')
studentinfo_reader = csv.DictReader(studentinfo_file)

for data in studentinfo_reader:
    # studentinfo_roll.append(data['Roll No'])
    # roll_in_studentinfo.append(data['Roll No'])
    
    studentinfo_data = { 
                        'rollno' : data['Roll No'],
                        'name'   : data['Name'],
                        'email'  : data['email'],
                        'aemail' : data['aemail'],
                        'contact' : data['contact']
                        }
    studentinfo_list.append(studentinfo_data)
# print(studentinfo_list)



# set_of_roll_in_studentinfo = set(roll_in_studentinfo)
# print(setof__roll_in_studentinfo)
studentinfo_df = pd.DataFrame(studentinfo_list)
# studentinfo_df
''' ---------------------------------------------------------------------------------------------  '''

course_registered_by_all_students_data = { }
course_registered_by_all_students_list = []
roll_in_registered = []
course_registered_by_all_students_file = open('course_registered_by_all_students.csv',mode = 'r')
course_registered_by_all_students_reader = csv.DictReader(course_registered_by_all_students_file)


for line in course_registered_by_all_students_reader:
    
    # roll_in_registered.append(line['rollno'])
    
    course_registered_by_all_students_data = {   
                                              'rollno'  : line['rollno'],
                                              'register_sem': line['register_sem'],
                                              'schedule_sem': line['schedule_sem'],
                                              'subno' : line['subno']
                                              
                                              }
    course_registered_by_all_students_list.append(course_registered_by_all_students_data)
# print(course_registered_by_all_students_list)


# set_of_roll_in_registered = set(roll_in_registered)
# print(set_of_roll_in_registered)
course_registered_by_all_students_df = pd.DataFrame(course_registered_by_all_students_list)
# course_registered_by_all_students_df

''' -------------------------------------------------------------------------------------------------- '''

# no_data_rolls = set_of_roll_in_registered - set_of_roll_in_studentinfo
# print(len(no_data_rolls),no_data_rolls)


joined_data = course_registered_by_all_students_df.join(studentinfo_df.set_index('rollno'), on='rollno')
joined_data = joined_data.fillna('NA_IN_STUDENTSINFO')
# joined_data.to_excel('joined_data.xlsx')
# joined_data


joined_data_bits = joined_data.join(course_master_data_df.set_index('subno'), on='subno')
# joined_data_bits
# joined_data_bits.to_excel('joined_data_bits.xlsx')


''' ------------------------------------------------------------------------------------------------------- '''


feedback_submitted_data = {}
feedback_submitted_list = []
feedback_submitted_file = open('course_feedback_submitted_by_students.csv')
feedback_submitted_reader = csv.DictReader(feedback_submitted_file)

for item in feedback_submitted_reader:
    feedback_submitted_data = { 
                               'name': item['stud_name'],
                               'rollno' : item['stud_roll'],
                               'subno' : item['course_code'], 
                               'feedback_type' : item['feedback_type'],
                               'prof_name'  : item['prof_name']
                               }
    feedback_submitted_list.append(feedback_submitted_data)
# print(feedback_submitted_list)

feedback_submitted_df = pd.DataFrame(feedback_submitted_list)
# feedback_submitted_df
feedback_submitted_df = feedback_submitted_df.drop_duplicates(subset=['name', 'rollno','subno','feedback_type'], keep='first')
# feedback_submitted_df
# feedback_submitted_df.to_excel('duplicates_removed.xlsx')


feedback_submitted_grp_df = feedback_submitted_df.groupby(['rollno','subno']).size().reset_index(name = 'frequency')
# feedback_submitted_grp_df
final_df = pd.merge(joined_data_bits,feedback_submitted_grp_df,how = 'outer', on =['rollno','subno'])
# final_df.head(100)
final_df = final_df.fillna(0)
# final_df
feedback_filled_indices  = final_df[ ( final_df['frequency'] >=final_df['non_zero_bits']) ].index

# feedback_filled_indices

final_df.drop(feedback_filled_indices,inplace = True)

final_df.drop(['non_zero_bits' , 'frequency'] , inplace =True ,axis = 1 )

final_df = final_df.reset_index()
final_df.drop(['index'],inplace  = True , axis =1)
final_df = final_df.set_index('rollno')
final_df.to_excel(output_file_name)