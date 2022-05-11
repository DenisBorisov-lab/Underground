import asyncio
import os
import random
import time


class Train:
    def __init__(self):
        self.passengers = []
        self.location = 0
        self.to_the_right = True

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
            await asyncio.sleep(right_time_motion[self.location])
            if self.location == 4:
                self.change_direction()
            else:
                self.location += 1
        else:
            await asyncio.sleep(left_time_motion[4 - self.location])
            if self.location == 0:
                self.change_direction()
            else:
                self.location -= 1

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
        self.passengers.append(random.choices(self.other_stations))


boost = float(input("Введите во сколько раз хотите ускорить время:"))
minute = 1 / boost
start = time.time()

stations = [Station("Рокоссовская", 0),
            Station("Соборная", 1),
            Station("Кристалл", 2),
            Station("Заречная", 3),
            Station("Библиотека им. Пушкина", 4)]

right_time_motion = [6 * minute, 3 * minute, 2 * minute, 7 * minute, 0]
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
        print(int((time.time() - start) / minute))
        for station in stations:
            print(f'{station.name}: {len(station.passengers)}')
        await asyncio.sleep(1)
        os.system("cls")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(show_details())
    loop.create_task(generate_passengers())
    loop.run_forever()
