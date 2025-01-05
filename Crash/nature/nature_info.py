from .nature import Nature


def show_nature():
    show_nature_info = Nature()
    a = show_nature_info.show_time()
    b = show_nature_info.show_weather()
    c = show_nature_info.show_temperature()
    return a, b, c


if __name__ == "__main__":
    show_nature()
