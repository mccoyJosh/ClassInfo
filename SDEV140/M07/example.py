from datetime import datetime


class Person:
    def __init__(self, f_name, l_name, gender, dob):
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        if '-' in dob:
            splits = dob.split('-')
            year_char = 'y'
            if len(splits[2]) == 4:
                year_char = 'Y'
            self.dob = datetime.strptime(dob, '%m-%d-%' + year_char)
        elif '/' in dob:
            splits = dob.split('/')
            year_char = 'y'
            if len(splits[2]) == 4:
                year_char = 'Y'
            self.dob = datetime.strptime(dob, '%m/%d/%' + year_char)
        else:
            print('INVALID DOB FORMAT: USE EITHER m/d/y or m-d-y')

    def get_age(self):
        time_rn = datetime.now()
        time_diff = time_rn.date().year.real - self.dob.date().year.real - 1
        if time_rn.month.real > self.dob.month.real:
            time_diff += 1
        elif time_rn.month.real == self.dob.month.real and time_rn.day.real >= self.dob.day.real:
            time_diff += 1
        return time_diff


