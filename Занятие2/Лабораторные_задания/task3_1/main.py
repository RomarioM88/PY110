def positive_check(fn):
    def wrapper(arg):
        # TODO написать проверку положительности аргумента arg
        if arg <= 0:
            raise ValueError("Аргумент функции не является положительным числом")
        else:
            return fn(arg)

    return wrapper


# TODO задекорировать функцию
@positive_check
def some_func(num: int):
    return num


if __name__ == "__main__":
    print(some_func(5))  # всё хорошо

    print(some_func(-5))  # должна быть вызвана ошибка ValueError
