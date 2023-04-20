def min_len_check(fn):
    # TODO записать обертку для исходной функции
    def wrapper(str):

        if len(str) <= 10:
            raise ValueError("Строка слишком короткая")
        else:
            return fn(str)

    return wrapper



# TODO задекорировать функцию
@min_len_check
def some_func(str_arg: str):
    return str_arg


if __name__ == "__main__":
    print(some_func("Hello, World!!!"))  # всё хорошо

    print(some_func("Short str"))  # ValueError("Строка слишком короткая")
