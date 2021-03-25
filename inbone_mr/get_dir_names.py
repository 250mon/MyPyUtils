import os
import datetime
from dateutil.relativedelta import relativedelta


def get_ids():
    dir = 'E:\\inbone MR\\'
    subdir = '\\DCMData\\'

    beg = datetime.datetime(2020, 6, 1)
    mons = [beg + relativedelta(months=i) for i in range(10)]
    # ['2020 06', '2020 07', ...]
    months = [m.strftime('%Y %m') for m in mons]
    # ['E"\\inbone MR\\2020 6\\DCMDATA\\' ...]
    dirnames = [dir + m + subdir for m in months]
    # {'2020 06': ['1000', '1001' ...], ...}
    ids = {mon: os.listdir(dirname) for mon, dirname in zip(months, dirnames)}

    # id is supposed to be a directory name
    # if the id is not a directory, but a file, remove it
    for k, v in ids.items():
        for i, id in enumerate(v):
            if os.path.isfile(dir + k + subdir + id):
                v.pop(i)

    #pprint.pprint(ids)
    return ids


if __name__ == '__main__':
    print(get_ids().keys())
