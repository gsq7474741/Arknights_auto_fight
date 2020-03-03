import subprocess
import time


class tap:
    x, y, t = 0, 0, 0

    def __init__(self, stp, doimm=False):
        self.x = stp[0]
        self.y = stp[1]
        self.t = stp[2]
        if doimm is True:
            self.do_tap()

    def do_tap(self):
        print('tapping ' + str(self.x) + r' ' + str(self.y))
        subprocess.Popen('adb shell input tap ' + str(self.x) + r' ' + str(self.y), shell=True)
        print('sleeping ' + str(self.t))
        time.sleep(self.t)
