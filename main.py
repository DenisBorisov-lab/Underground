import asyncio
import os
import random
import signal
import time

import animation
import statistics


def signal_handler(signal, frame):
    os.system("cls")
    plot.draw_graph()
    exit(0)


class Train:
    def __init__(self):
        self.passengers = []
        self.location = 0
        self.to_the_right = True
        self.spaces = 0

    def drop_passengers(self):
        survived_passengers = []
        for passenger in self.passengers:
            if passenger != self.location:
                survived_passengers.append(passenger)
        self.passengers = survived_passengers

    def boarding_passengers(self):

        waiting_passengers = []

        for passenger in stations[self.location].passengers:
            if len(self.passengers) < 400:
                if self.to_the_right:
                    if passenger > self.location:
                        self.passengers.append(passenger)
                    else:
                        waiting_passengers.append(passenger)
                else:
                    if passenger < self.location:
                        self.passengers.append(passenger)
                    else:
                        waiting_passengers.append(passenger)
            else:
                waiting_passengers.append(passenger)

        stations[self.location].passengers = waiting_passengers

    def change_direction(self):
        self.to_the_right = False if self.to_the_right else True

    async def get_to_next_station(self):
        if self.to_the_right:
            # await asyncio.sleep(right_time_motion[self.location])
            for _ in range(len(right_time_motion)):
                self.spaces += 1
                await asyncio.sleep(minute)
            if self.location == 4:
                self.change_direction()
            else:
                self.location += 1
                self.spaces += 1
        else:
            # await asyncio.sleep(left_time_motion[4 - self.location])
            for _ in range(len(left_time_motion)):
                self.spaces -= 1
                await asyncio.sleep(minute)
            if self.location == 0:
                self.change_direction()
            else:
                self.location -= 1
                self.spaces -= 1

    async def run(self):
        while True:
            self.drop_passengers()
            self.boarding_passengers()
            await asyncio.sleep(minute / 4)
            await self.get_to_next_station()


class Station:
    def __init__(self, name, index):
        self.passengers = []
        self.name = name
        self.index = index
        self.other_stations = [0, 1, 2, 3, 4]
        del self.other_stations[index]

    def generate_passenger(self):
        to = random.choices(self.other_stations)[0]
        self.passengers.append(to)
        plot.passengers_deploy_in_sec.append([self.index, to])


boost = float(input("Введите во сколько раз хотите ускорить время:"))
minute = 1 / boost
start = time.time()

stations = [Station("Рокоссовская", 0),
            Station("Соборная", 1),
            Station("Кристалл", 2),
            Station("Заречная", 3),
            Station("Библиотека им. Пушкина", 4)]

right_time_motion = [6, 3 , 2 , 7 , 0]
left_time_motion = list(reversed(right_time_motion))
time_to_drop_passengers = minute * 0.25


async def generate_passengers():
    await asyncio.sleep(minute * 18)
    while True:
        for station in stations:
            station.generate_passenger()
        await asyncio.sleep(minute / 60)


async def show_details():
    while True:
        # print(int((time.time() - start) / minute))
        amount_of_platform_passengers = 0
        for station in stations:
            # print(f'{station.name}: {len(station.passengers)}')
            amount_of_platform_passengers += len(station.passengers)
        average_platform_passengers = amount_of_platform_passengers / len(stations)
        plot.average_platform_passengers.append(average_platform_passengers)

        amount_of_passengers = 0
        for train in trains:
            # print(f'поезд находится на станции {stations[train.location].name} и в нём {len(train.passengers)}')
            amount_of_passengers += len(train.passengers)
        plot.average_passengers.append(amount_of_passengers / len(trains))

        plot.cut()

        await asyncio.sleep(1)
        os.system("cls")


plot = statistics.Statistics(minute)
trains = []
amount_of_trains = int(input("Введите количество поездов: "))


async def generate_trains():
    for i in range(amount_of_trains):
        trains.append(Train())
        loop.create_task(trains[i].run())
        await asyncio.sleep(minute * 38 / amount_of_trains)


if __name__ == "__main__":
    animation.define_start(start, minute)
    signal.signal(signal.SIGINT, signal_handler)
    loop = asyncio.get_event_loop()
    loop.create_task(generate_passengers())
    loop.create_task(generate_trains())
    loop.create_task(show_details())
    loop.create_task(animation.graphics(trains, stations))
    loop.run_forever()
