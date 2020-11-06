from time import sleep
import pyautogui as pg
import functools


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


class FluVaccineEdu:
    def __init__(self):
        pg.PAUSE = 1
        pg.FAILSAFE = True

        self.img_dir = 'C:\\Users\\inbon\\Pictures\\'
        self.screen_region = (0, 0, 1060, 800)

    def imgFileName(self, name):
        return self.img_dir + name + '.png'

    def clickAt(self, pos):
        org_pos = pg.position()
        pg.click(pos)
        pg.moveTo(org_pos, duration=0.1)

    def isImgFound(self, names):
        for name in names:
            pos = pg.locateCenterOnScreen(self.imgFileName(name), region=self.screen_region)
            if pos != None:
                break
        return pos

    def isImgFoundAll(self, names):
        for name in names:
            pos = list(pg.locateAllOnScreen(self.imgFileName(name), region=self.screen_region))
            if len(pos) != 0:
                break
        return pos

    def run(self):
        newScreen = True
        try:
            while (True):
                posNext = self.isImgFound(['next', 'next2', 'next3'])
                posEnd1 = self.isImgFound(['end1', 'end11'])
                posEnd2 = self.isImgFound(['end2', 'end21'])
                posAbNext = self.isImgFound(['ab_next'])
                posAbClicks = self.isImgFoundAll(['ab_click', 'ab_click2'])
                posMis = self.isImgFoundAll(['mi'])
                # when only one "mi" button is left, it means that the session is over
                if len(posMis) <= 1:
                    pass
                    #print('Finished')

                # when "next" button is activated, press it
                if posNext != None:
                    self.clickAt(posNext)
                    newScreen = True
                # when "green next" button is activated, press it
                elif posAbNext != None:
                    self.clickAt(posAbNext)
                # when the chapter gets to the end, press the second "mi" button
                elif posEnd1 != None and posEnd2 != None:
                    pass
                    #self.clickAt(posMis[1])
                # when a series of "click" buttons are activated, press them one by one
                elif newScreen and len(posAbClicks) != 0:
                    for abClick in posAbClicks:
                        self.clickAt(abClick)
                        sleep(2)
                    newScreen = False
                else:
                    pass
                sleep(3)
        except KeyboardInterrupt:
            print('\nTerminated.')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flu = FluVaccineEdu()
    flu.run()

