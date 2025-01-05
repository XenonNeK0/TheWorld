import random


def weather_random():
    num = random.randint(0, 90)
    if 0 <= num < 30:
        a = "Sunny"
        return a
    elif 30 <= num < 60:
        b = "Rain"
        return b
    elif 60 <= num <= 90:
        c = "Cloudy"
        return c


if __name__ == "__main__":
    a = weather_random()
    print(a)
