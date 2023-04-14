def task() -> list:
    temp_tuple = (0, 36.6, 100)
    temp_far = []
    for t in temp_tuple:
        f = t * 1.8 + 32
        temp_far.append(f)
    return temp_far  # TODO  вернуть список температур по Фаренгейту


if __name__ == "__main__":
    print(task())
temperatures_celsius = [25, 30, 15, 20, 10]
temperatures_fahrenheit = []

