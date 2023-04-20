def pow_gen(base: int):
    st = 1
    while True:
        yield st
        st = st * base

# TODO записать функцию-генератор


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
