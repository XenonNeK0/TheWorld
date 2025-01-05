import time
from weather_option import weather_random
from temperature_option import temperature_now


class Nature:
    def __init__(self):
        self.time = time.localtime()
        self.weather = weather_random()
        self.temperature = temperature_now()

    def show_time(self):
        formatted_time = time.strftime("%H:%M:%S", self.time)
        print(formatted_time)

    def show_weather(self):
        print(self.weather)

    def show_temperature(self):
        print(self.temperature)


if __name__ == "__main__":
    a = Nature()
    a.show_time()
    a.show_weather()
    a.show_temperature()
