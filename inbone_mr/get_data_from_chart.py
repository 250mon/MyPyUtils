from time import sleep
import pyautogui as pg
import functools
import pyperclip
import pt_data


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        with open('log.txt', 'a') as f:
            f.write(f'TRACE: calling {func.__name__}() '
                    f'with {args}, {kwargs}\n')
            f.write(f'TRACE: {func.__name__}() '
                    f'returned {original_result!r}\n\n')
        return original_result

    return wrapper


class DataFromChart:
    def __init__(self):
        pg.PAUSE = 1
        pg.FAILSAFE = True
        pyperclip.copy('')

        self.img_dir = 'D:\\temp\\inbone_chart_images\\'
        self.screen_region = (0, 0, 1060, 800)

    def imgFileName(self, name):
        return self.img_dir + name + '.png'

    # returns the coordinates of the image
    # if not found, returns None
    def img_location(self, name):
        # pos = pg.locateCenterOnScreen(self.imgFileName(name), region=self.screen_region)
        pos = pg.locateCenterOnScreen(self.imgFileName(name))
        return pos

    def input_id(self, id, point):
        try:
            # location of the button for a chart id to be input
            pos_id = (point)
            pg.click(pos_id, clicks=2, interval=0.05)
            pg.typewrite(['backspace'] * 4)
            pg.typewrite(id + '\n', interval=0.0)
        except KeyboardInterrupt:
            print('\nTerminated.')

    def copy_at(self, point=None):
        try:
            if point != None:
                pg.click(point)
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            pyperclip.paste()
        except KeyboardInterrupt:
            print('\nTerminated.')

    def get_pt_info_from_gui(self, pt_data):
        # Retrieve pt info
        # point of id input box in chart viewer to retrieve pt info
        id = pt_data.get_id()
        id_pos = (110, 156)
        self.input_id(id, id_pos)

        # no pt info msg box
        pg.click((543, 546))

        # name
        self.copy_at((115, 187))
        nm = pyperclip.paste()
        pt_data.set_name(nm)

        # social number
        self.copy_at((178, 220))
        social = pyperclip.paste()
        pt_data.set_socialnumber(social)
        #pt_data.handle_socialnumber(pyperclip.paste())

    def get_contents_from_gui(self, pt_data):
        # click the center of the window title bar to activate the window
        pg.click(760, 15)

        # Retrieve pt contents
        # point of id input box in main chart to retrieve pt contents
        id = pt_data.get_id()
        id_pos = (100, 80)
        self.input_id(id, id_pos)

        # cancel the save button of the previous pt
        pg.click(1020, 600)

        try:
            # location of the window where the contents are shown
            sleep(0.1)
            pg.click(382, 626, clicks=2, interval=0.5)
            self.copy_at()
            # pg.hotkey('ctrl', 'a')
            # pg.click(377, 978, clicks=2, interval=0.1)
            # sleep(0.2)

            # Copy the contents to the clipboard
            self.copy_at()
            # Paste the contents to the pt_data
            pt_data.set_contents(pyperclip.paste())
        except KeyboardInterrupt:
            print('\nTerminated.')


if __name__ == '__main__':
    dfc = DataFromChart()
    pt = pt_data.PtData('2020 6', '1377')

    dfc.get_contents_from_gui(pt)
    # name = pt.get_name()
    # sn = pt.get_socialnumber()
    # print(f'name = {name}')
    # print(f'sn = {sn}')
    ct = pt.get_contents()
    print(f'ct = {ct}')
    #dfc.get_contents_from_gui(pt)
    #print(pt.get_contents())
