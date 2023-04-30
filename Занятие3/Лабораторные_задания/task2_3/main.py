import json


def task():
    filename = "input.json"
    with open(filename, 'r') as f:
        js_l = json.load(f)  # TODO считать содержимое JSON файла
    # print(js_l)
    key_f = lambda record: record['score']
    max_record = max(js_l, key=key_f)
    # print(max_record)
    return max_record  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
