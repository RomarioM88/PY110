import json


def task(input_filename: str, output_filename: str) -> None:
    #js_in = json.dumps(input_file, ensure_ascii=False, indent=4)  # TODO считать содержимое json файл input.json
    with open(input_file, 'r') as f:
        data = json.load(f)
    with open(output_file, 'w') as f2:
        f2.write(json.dumps(data, ensure_ascii=False, indent=4))  # TODO записать содержимое в json файл output.json с отступами


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
