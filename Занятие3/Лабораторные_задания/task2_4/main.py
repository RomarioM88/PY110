import json


def task():
    filename = "input.json"
    with open(filename, 'r') as f:
        js_l = json.load(f)  # TODO считать содержимое JSON файла
    #print(js_l)
    key = "contains_improvement_appeals"
    gen_exr = sum(item[key] for item in js_l)
    # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return gen_exr


if __name__ == "__main__":
    print(task())
