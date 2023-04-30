INPUT_FILE = "input.txt"


def task() -> None:
    with open('input.txt', 'r') as file:  # TODO открыть указатель на файл
        for word in file:
            print(word, end='')

# TODO файл является итератором, который работает с циклом for в построчном режиме


if __name__ == "__main__":
    task()
