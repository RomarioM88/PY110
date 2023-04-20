def make_string_upper(fn):
    def wrapper(str):
        # TODO перевести результат исходной функции в верхний регистр

        result = fn(str)
        return result.upper()

    return wrapper


@make_string_upper
def get_text(str) -> str:
    return "Hello, World!!!"


if __name__ == "__main__":
    print(get_text(1))
