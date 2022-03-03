from time import sleep
from itertools import cycle


class TrafficLight:

    states = [("red", 7, "\033[31m"), ("yellow", 2, "\033[93m"), ("green", 7, "\033[32m"), ("yellow", 2, "\033[93m")]

    def __init__(self):
        # В текущей реализации делать этот атрибут нет необходимости, но требуется по заданию.
        self.__color = self.states[0]

    def running(self):
        for state in cycle(self.states):
            color_str, sleep_time, color_ptr = state
            print(color_ptr, color_str)
            self.__color = color_str
            sleep(sleep_time)


trafficLight = TrafficLight()
trafficLight.running()
