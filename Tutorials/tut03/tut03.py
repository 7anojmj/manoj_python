import os

def output_individual_roll(f):
    data_of_roll = {}
    folder_name = "output_individual_roll"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for row in f:
        titles = row.strip().split(",")
        rollno, register_sem, schedule_sem, subno, grade1, date_of_entry1, grade2, date_of_entry2, sub_type = titles
        if rollno not in data_of_roll:
            data_of_roll[rollno] = []
        data_of_roll[rollno].append([rollno, register_sem, subno, sub_type])

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for rollno in data_of_roll:
        fdata=data_of_roll[rollno]
        file_name=  os.path.join(folder_name, rollno + ".csv")
        with open(file_name, "w") as f:
            f.write('rollno, register_sem, subno, sub_type\n')
            f.write("\n".join((",".join(rdata)) for rdata in fdata))


def output_by_subject(f):
    data_of_subjects = {}
    folder_name = "output_by_subject"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for row in f:
        titles = row.strip().split(",")
        rollno, register_sem, schedule_sem, subno, grade1, date_of_entry1, grade2, date_of_entry2, sub_type = titles
        if subno not in data_of_subjects:
            data_of_subjects[subno] = []
        data_of_subjects[subno].append([rollno, register_sem, subno, sub_type])

    for subno in data_of_subjects:
        fdata=data_of_subjects[subno]
        file_name=  os.path.join(folder_name, subno + ".csv")
        with open(file_name, "w") as f:
            f.write('rollno, register_sem, subno, sub_type\n')
            f.write("\n".join((",".join(rdata)) for rdata in fdata))

with open('regtable_old.csv', mode='r') as data:
    lines = data.readlines()
    # print(lines)
    output_by_subject(lines)
    output_individual_roll(lines)

