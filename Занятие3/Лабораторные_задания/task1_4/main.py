INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as f1:
        with open(OUTPUT_FILE, 'w') as f2:

            for line in f1:
                f2.write(line.upper())
#f2.write[line for line in f1 line.upper()]

# TODO перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
