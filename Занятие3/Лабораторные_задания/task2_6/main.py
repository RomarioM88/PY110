import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)
    key_f = lambda record: record['length']
    sort = sorted(json_data, key=key_f) # TODO отсортировать список словарей

    with open('output.json', 'w') as f:
        f.write(json.dumps(sort, ensure_ascii=False, indent=4)) # TODO дополнительно записать отсортированный список в JSON файл
    return sort


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))


