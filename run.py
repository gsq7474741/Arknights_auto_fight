import copy
import json
import time

import screen_read
import sim_tap


# img5 = Image.open('test5.png')
#
# box_start = (1830, 967, 1890, 1020)
# imgs = img5.crop(box_start)
# imgs.show()


def step(tap_coordinates, time_series):
    for i in range(len(time_series)):
        stp = tap_coordinates[i]
        stp.append(time_series[i])
        yield stp


def main0():
    config = json.load(open('config.json', 'r'))
    count = config['pause']
    level_name = config['level']
    to_do_times = config['times']
    print('Todo ' + level_name + ' from ' + str(count) + ' to ' + str(to_do_times) + ' times.')
    with open('log.txt', 'a') as log:
        log.write('ToDo ' + level_name + ' from ' + str(count) + ' to ' + str(to_do_times) + ' times.\n')
    while True:
        if count >= to_do_times:
            break
        queue = step(copy.deepcopy(config['levels']['xy']), copy.deepcopy(config['levels'][level_name]['t']))
        while True:
            try:
                stp = next(queue)
                print(stp)
                time.sleep(1)
                atap = sim_tap.tap(stp)
                atap.do_tap()
            except StopIteration:
                count += 1
                with open('log.txt', 'a') as log:
                    log.write(
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' Finsih ' + level_name + ' ' + str(
                            count) + ' times.\n')
                print('Finsih ' + level_name + ' ' + str(count) + ' times.')
                break
    print('Finished All.')


def main():
    config = json.load(open('config.json', 'r'))
    count = config['pause']
    level_name = config['level']
    to_do_times = config['times']
    print('Todo ' + level_name + ' from ' + str(count) + ' to ' + str(to_do_times) + ' times.')
    with open('log.txt', 'a') as log:
        log.write('ToDo ' + level_name + ' from ' + str(count) + ' to ' + str(to_do_times) + ' times.\n')
    while True:
        if count >= to_do_times:
            break
        if config["isAutoT"] is True:
            queue = step(copy.deepcopy(config['levels']['autoLevel']['xy']),
                         copy.deepcopy(config['levels']['autoLevel']['t']))
        else:
            queue = step(copy.deepcopy(config['levels']['xy']), copy.deepcopy(config['levels'][level_name]['t']))
        # queue = config['levels']['xy']
        while True:
            try:
                stp = next(queue)
                # print(stp)
                time.sleep(1)
                if stp[0] == 1822:
                    print('Pre sleeping ' + str(config['preSleep']))
                if stp[0] == 1917:
                    time.sleep(config['preSleep'])
                    tryTimes = 0
                    while True:
                        if tryTimes > 10:
                            sim_tap.tap([1122, 100, 0], doimm=True)
                        scr = screen_read.Scrr()
                        if scr.ifEnd is False:
                            tryTimes += 1
                            print(scr.ifEnd)
                            print('sleeping 7s')
                            time.sleep(7)
                        else:
                            print(scr.ifEnd)
                            break
                atap = sim_tap.tap(stp)
                atap.do_tap()
            except StopIteration:
                count += 1
                with open('log.txt', 'a') as log:
                    log.write(
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' Finsih ' + level_name + ' ' + str(
                            count) + ' times.\n')
                print('Finsih ' + level_name + ' ' + str(count) + ' times.')
                break
    print('Finished All.')


if __name__ == '__main__':
    main()
