from pt_data import PtData
import get_dir_names
import xl_db
from get_data_from_chart import DataFromChart
from time import sleep
import pyperclip

def save_pt_data(mon, pt_list):
    print("Saving...")
    # bring up workbook
    xl_wb = xl_db.XlDb('D:\\test_main.xlsx')  # 'inbone_mr.xlsx'
    # get the worksheet for mon
    ws = xl_wb.create_sht(mon)
    # write the pt data to the worksheet
    for pt_data in pt_list:
        xl_wb.write_record_by_id(ws, pt_data, contents=True)
    # save the xl file for a check point
    xl_wb.save_wb()

if __name__ == '__main__':
    dfc = DataFromChart()
    ids = get_dir_names.get_ids()

    headings = ['date', 'id', 'sn', 'name', 'gender', 'age', 'contents']

    dfc = DataFromChart()
    sleep(0.5)

    pt_list = []
    # pt2 = PtData('2020 6', '1316')
    # pt1 = PtData('2020 6', '1377')
    # pts = [pt1, pt2]
    # for pt in pts:
    # #    dfc.get_pt_info_from_gui(pt)
    #     dfc.get_contents_from_gui(pt)
    #     pt_list.append(pt)
    # # bring up workbook
    # xl_wb = xl_db.XlDb('D:\\test_main.xlsx')  # 'inbone_mr.xlsx'
    # # create a new worksheet
    # ws = xl_wb.create_sht('2020 06', col_headings=headings)
    # # write the pt data to the worksheet
    # for pt_data in pt_list:
    #     #xl_wb.write_record(ws, pt_data)
    #     xl_wb.write_record_by_id(ws, pt_data, contents=True)
    # # save the xl file for a check point
    # xl_wb.save_wb()
    # exit(0)

    # retrieve pt info and save it to the xldb in the monthly basis
    # for mon, id_list in ids.items():
    #     # create pts and retrieve pt info
    #     for id in id_list:
    #         print(mon + ' ' + id)
    #         # create a pt
    #         pt = PtData(mon, id)
    #         # retrieve the pt info
    #         dfc.get_pt_info_from_gui(pt)
    #         # add the pt to the list
    #         pt_list.append(pt)
    #         sleep(0.1)
    #
    #     # bring up workbook
    #     xl_wb = xl_db.XlDb('D:\\test_main.xlsx')  # 'inbone_mr.xlsx'
    #     # create a new worksheet
    #     ws = xl_wb.create_sht(mon, col_headings=headings)
    #     # write the pt data to the worksheet
    #     for pt_data in pt_list:
    #         xl_wb.write_record(ws, pt_data)
    #     # save the xl file for a check point
    #     xl_wb.save_wb()
    #     pt_list.clear()

    # # retrieve pt contents and save it to the xldb in the monthly basis
    initial_point = 25
    check_point = 3
    for mon, id_list in ids.items():
        # create pts and retrieve pt contents
        if mon in [
            '2020 06',
            '2020 07',
            '2020 08',
            '2020 09',
            '2020 10',
            #'2020 11',
            '2020 12',
            '2021 01',
            #'2021 02',
            #'2021 03',
        ]:
            continue
        total = len(id_list)
        for i, id in enumerate(id_list):
            # skip upto initial_point
            if i < initial_point:
                continue
            print(f'{i}/{total}: {mon} {id}')
            # create a pt
            pt = PtData(mon, id)
            # retrieve the pt contents
            dfc.get_contents_from_gui(pt)
            # add the pt to the list
            pt_list.append(pt)
            # save at every check point
            if i != 0 and i % check_point == 0:
                save_pt_data(mon, pt_list)
                pt_list.clear()
        # save the remaining
        if pt_list is not None:
            save_pt_data(mon, pt_list)
            pt_list.clear()
        initial_point = 0



