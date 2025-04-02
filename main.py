import openpyxl
import pandas as pd
from student import Student

def action(name, age):
    if age == '1 класс':
        age = '1'
    elif age == '2-3 класс':
        age = '23'
    elif age == '4-5 класс':
        age = '45'
    elif age == '6-7 класс':
        age = '67'
    elif age == '8-11 класс':
        age = '811'
    #["1 класс", "2-3 класс", "4-5 класс", '6-7 класс', '8-11 класс']
    wb = openpyxl.load_workbook(name)
    sp_list = wb.sheetnames

    df = pd.read_excel(name, sheet_name=f"{sp_list[0]}")
    df1 = pd.read_excel(name, sheet_name=f"{sp_list[1]}")

    students = {}
    sp = []

    for i in range(len(df)):
        class_student = Student(df.iloc[i]['ФИО'], age)
        class_student.individual(df.iloc[i])
        students[f'{df.iloc[i]['ФИО']}'] = class_student
        #print(class_student.println())

    for i in range(2, len(df1)):
        #print(df1.iloc[i])
        fio = df1.iloc[i]['ФИО'].split()[:2]
        id = ''
        for j in students:
            temp = j.split()
            temp = ' '.join(temp[:2])
            if fio[0] in temp and fio[1] in temp:
                id = j
                break
        if id != '':
            print(fio,  id, students[id].println())
            #print(df1.iloc[i])
            students[id].group(df1.iloc[i])
            print(fio,  id, students[id].println())
            print('#############################')
        else:
            print(f'{fio} не найден!')
            sp.append(fio[0] + ' ' + fio[1])

    data = []
    for i in students:
        data.append(students[i].println())
    new_df = pd.DataFrame(data)
    return [new_df, sp]




