import asyncio
import os
import time

TimeToStations = [0, 6, 3, 2, 7]

StartTime = 0
Minute = 0


def define_start(start, minute):
    global StartTime
    global Minute
    StartTime = start
    Minute = minute


async def graphics(trains, stations):
    while True:
        os.system('cls')
        current_time = int((time.time() - StartTime) / Minute)
        start_str = f'Time elapsed: ' + str(current_time) + '\n'
        start_str += str(len(stations[0].passengers)) + ' ' * (14 - len(str(len(stations[0].passengers))))
        start_str += str(len(stations[1].passengers)) + ' ' * (8 - len(str(len(stations[1].passengers))))
        start_str += str(len(stations[2].passengers)) + ' ' * (6 - len(str(len(stations[2].passengers))))
        start_str += str(len(stations[3].passengers)) + ' ' * (16 - len(str(len(stations[3].passengers))))
        start_str += str(len(stations[4].passengers))
        start_str += '\n'
        # start_str += 'R -  -  -  -  -  -S -  -  -  K -  -  Z -  -  -  -  -  -  -  B\n'
        start_str += 'R - - - - - - S - - - K - - Z - - - - - - - B\n'
        for train in trains:
            spaces = train.spaces
            start_str += '  ' * spaces + '🚂' + str(len(train.passengers)) + '\n'
        print(start_str)
        await asyncio.sleep(1/25)