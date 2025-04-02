import data

class Student:
    def __init__(self, name_sername, age):
        self.name = name_sername.split()[1]
        self.sername = name_sername.split()[0]
        if age == '1':
            self.komp = data.komp1
            self.res = {'Имя': self.name,
                        'Фамилия': self.sername,
                        'логические действия': 0,
                        'критическое мышление': 0,
                        'креативное мышление': 0,
                        'коммуникация': 0,
                        'коллаборация': 0,
                        'управление мотивацией и эмоциями': 0,
                        'самоорганизация': 0,
                        'общий балл': 0,
                        }

            self.group_res = data.sl_1_group
            self.indvidual_res = data.sl_1_individ

        elif age == '23':
            self.komp = data.komp23
            self.res = {'Имя': self.name,
                        'Фамилия': self.sername,
                        'логические действия': 0,
                        'критическое мышление': 0,
                        'креативное мышление': 0,
                        'коммуникация': 0,
                        'коллаборация': 0,
                        'планирование': 0,
                        'управление мотивацией и эмоциями': 0,
                        'самоорганизация': 0,
                        'общий балл': 0,
                        }
            self.group_res = data.sl_23_group
            self.indvidual_res = data.sl_23_individ
        else:
            self.komp = data.komp411
            self.res = {'Имя': self.name,
                        'Фамилия': self.sername,
                        'логические действия': 0,
                       'критическое мышление': 0,
                       'креативное мышление': 0,
                       'коммуникация': 0,
                       'коллаборация': 0,
                       'целеполагание': 0,
                       'планирование': 0,
                       'саморегуляция': 0,
                       'самооценивание и рефлексия': 0,
                       'общий балл': 0,
                       }
            self.group_res = data.sl_group
            if age == '45':
                self.indvidual_res = data.sl_45_individ
            elif age == '67':
                self.indvidual_res = data.sl_67_individ
                del self.res['саморегуляция']
            elif age == '811':
                self.indvidual_res = data.sl_811_individ
                del self.res['саморегуляция']




    def individual(self, data):
        n = len(self.indvidual_res)
        #print(1, data[-n])
        if ',' in str(data[-n]):
            res = [int(i.split(',')[0]) for i in list(data[-n:])]
        else:
            res = [int(i) for i in list(data[-n:])]
        #print(res)
        for i in range(1, len(self.indvidual_res) + 1):
            name_komp = self.komp[self.indvidual_res[i - 1]]
            self.res[name_komp] += res[i - 1]
       # print('ind', self.res)

    def group(self, data):
        fio = ''
        marks = []
        for j in data:
            if fio == '':
                fio = j
            else:
                marks.append(int(j))
        for i in range(len(self.group_res)):
            name_komp = self.komp[self.group_res[i]]
            self.res[name_komp] += marks[i]
        #print('group', self.res)

    def println(self):
        summ = 0
        for i in list(self.res.keys())[2: -1]:
            summ += self.res[i]
        self.res['общий балл'] = summ
        return self.res