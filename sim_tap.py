import time
import subprocess
import tqdm
import pandas as pd


class tap:
    x, y, t = 0, 0, 0

    def __init__(self, stp):
        self.x = stp[0]
        self.y = stp[1]
        self.t = stp[2]

    def do_tap(self):
        print('tapping ' + str(self.x) + r' ' + str(self.y))
        subprocess.Popen('adb shell input tap ' + str(self.x) + r' ' + str(self.y), shell=True)
        print('sleeping ' + str(self.t))
        # for i in tqdm.trange(self.t):
        time.sleep(self.t)
        # subprocess.Popen('adb shell input tap '+x+r' '+y, shell=True)
        # time.sleep(3)
        # subprocess.Popen('adb shell input tap ', shell=True)


# /storage/self/primary/screen_caps
# start = [(1830, 967), (1890, 967), (1830, 1020), (1890, 1020)]
# ax = 1844
# ay = 870
