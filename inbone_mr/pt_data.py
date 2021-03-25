import datetime


class PtData:
    def __init__(self, month, id):
        self.month = month  # '2020 6'
        self.id = id
        self.socialnumber = None
        self.name = None
        self.gender = None
        self.age = None
        self.contents = None

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_contents(self, contents):
        self.contents = contents

    def get_contents(self):
        return self.contents

    def get_data_list(self):
        return [self.month, self.id, self.socialnumber, self.name, self.gender, self.age, self.contents]

    def set_socialnumber(self, sn):
        self.socialnumber = sn

    def get_socialnumber(self):
        return self.socialnumber

    # social number: 720101-1******
    def handle_socialnumber(self, sn):
        # convert the first part of a social number to datetime format
        yr = sn[:2]
        yr = '19' + yr if int(yr) > 10 else '20' + yr
        yr = int(yr)
        mo = int(sn[2:4])
        da = int(sn[4:6])
        birth_date = datetime.datetime(yr, mo, da, 0, 0, 0)

        # extract gender from a social number
        gd = sn[7]
        gd_num = int(gd)
        gd = 'F' if gd_num % 2 == 0 else 'M'
        self.set_gender(gd)

        # convert self.month to datetime format
        yr = int(self.month[:4])
        mo = int(self.month[5:])
        mr_date = datetime.datetime(yr, mo, 1, 0, 0, 0)

        print(birth_date, mr_date)
        delta = mr_date - birth_date
        self.set_age(delta)


if __name__ == '__main__':
    ptData = PtData('2020 6', '1000')
    ptData.handle_socialnumber('720102-2233333')
