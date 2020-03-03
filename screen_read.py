from PIL import Image
import os
import subprocess
import time


class Scrr():
    def __init__(self):
        self.img = self.get_cap()
        self.ifEnd = self.is_end(self.img)

    def get_cap(self):
        capPath = './caps/tmp.jpg'
        doCap = subprocess.Popen('adb shell screencap -p /storage/emulated/0/tmp.jpg', shell=True,
                                 stdout=subprocess.PIPE)
        while True:
            if doCap.stdout.readline() is not None:
                break
        # time.sleep(1)
        doPull = subprocess.Popen('adb pull /storage/emulated/0/tmp.jpg ' + capPath, shell=True, stdout=subprocess.PIPE)
        while True:
            if doPull.stdout.readline() is not None:
                break
        # time.sleep(1)
        img = Image.open(capPath)
        return img

    def is_end(self, img):
        xs = [(266, 383, 497), 770]
        ys = [(271, 388, 502), 775]

        boxes = []
        for i in range(len(xs[0])):
            box = [xs[0][i], xs[1], ys[0][i], ys[1]]
            boxes.append(box)

        crops = []
        for box in boxes:
            imc = img.crop(box)
            crops.append(imc)

        rgs = []
        for imc in crops:
            for j in range(5):
                r, g = imc.getpixel((j, j))[0], imc.getpixel((j, j))[1]
                rg = [r, g]
                rgs.append(rg)
                # print(imc.getpixel((j, j)))

        for rg in rgs:
            if rg[0] < 66 and rg[0] > 60:
                if rg[1] > 230:
                    continue
                else:
                    return False
            else:
                return False

        return True


def main():
    start = time.time()
    scr = Scrr()
    ifend = scr.ifEnd
    print(ifend)
    print(time.time() - start)


# if __name__ == '__main__':
#     main()
