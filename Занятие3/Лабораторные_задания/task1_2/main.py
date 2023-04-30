OUTPUT_FILE = "output.txt"


def task():
    n = 10
    for i in range(1, n+1):
        print(" " * (10-i) + "*" * i)

    #TODO записать лесенку в файл


if __name__ == "__main__":
    task()


    with open("output.txt", 'w') as f:
        n = 10
        for i in range(n):
            line = " " * (10-i) + "*" * i + '\n'
            f.write(line)