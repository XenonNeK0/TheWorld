import random
from .weather_option import weather_random


def temperature_now():
    weather_now = weather_random()
    if weather_now == "Sunny":
        tempearture = random.randint(25, 30)
        return tempearture
    elif weather_now == "Rain":
        tempearture = random.randint(15, 20)
        return tempearture
    elif weather_now == "Cloudy":
        tempearture = random.randint(20, 25)
        return tempearture


if __name__ == "__main__":
    a = temperature_now()
    print(a)
