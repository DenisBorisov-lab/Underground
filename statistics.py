class Statistics:
    time_to_stations = [6, 3, 2, 7]

    def __init__(self, minute):
        self.average_platform_passengers = []
        self.average_passengers = []
        self.average_time = []
        self.passengers_deploy_in_sec = []
        self.minute = minute

    def cut(self):
        self.average_time.append(self.passengers_deploy_in_sec)
        self.passengers_deploy_in_sec = []

    def draw_plot(self):
        self.reformat_average_time()
        seconds = []
        for _ in range(len(self.average_platform_passengers)):
            seconds.append(_ * 1 / self.minute)
        print(self.average_platform_passengers)
        print(self.average_passengers)
        seconds2 = []
        for _ in range(len(self.average_time)):
            seconds2.append(_ * 1 / self.minute + 18)
        print(self.average_time)

    def reformat_average_time(self):
        times = []
        for second in self.average_time:
            numbers = []
            if len(second) == 0:
                continue
            for elem in second:
                if elem[0] < elem[1]:
                    numbers.append(sum(self.time_to_stations[elem[0]: elem[1] - 1]) + (elem[1] - elem[0]) * 0.25)
                else:
                    numbers.append(sum(self.time_to_stations[elem[1]: elem[0] - 1]) + (elem[0] - elem[1]) * 0.25)
            times.append(sum(numbers) / len(numbers))

        self.average_time = times
