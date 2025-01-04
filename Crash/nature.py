import time


class Nature:
    def __init__(self, weather, temperature):
        self.time = time.localtime()
        self.weather = weather
        self.temperature = temperature

    def show_time(self):
        formatted_time = time.strftime("%H:%M:%S", self.time)
        print(formatted_time)


if __name__ == "__main__":
    a = Nature(1, 2)
    b = a.show_time()
    print(b)
