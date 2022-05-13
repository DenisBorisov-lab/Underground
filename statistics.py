import matplotlib.pyplot as plt


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

    def draw_graph(self):

        self.reformat_average_time()
        seconds = []
        for _ in range(len(self.average_platform_passengers)):
            seconds.append(_ * 1 / self.minute)
        seconds2 = []
        for _ in range(len(self.average_time)):
            seconds2.append(_ * 1 / self.minute + 18)

        fig, (StationsGraph,
              TrainsGraph,
              TransportGraph) = plt.subplots(nrows=1, ncols=3, sharex=True, figsize=(13, 6))

        line1, = StationsGraph.plot(seconds, self.average_platform_passengers, linewidth=0.6)

        StationsGraph.set_title('Average platform passengers')

        TrainsGraph.plot(seconds, self.average_passengers)
        TrainsGraph.set_title('Average passengers')

        TransportGraph.plot(seconds2, self.average_time)
        TransportGraph.set_title('Average transport time')

        plt.tight_layout()
        plt.show()
