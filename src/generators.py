def my_range(start, end=None, step=1):
    if not end:
        end = start
        start = 0

    while start < end:
        yield start
        start += step


if __name__ == '__main__':  # pragma: no cover
    for x in my_range(4):
        print(x)

    for x in my_range(2, 5):
        print(x)

    for x in my_range(0, 8, 2):
        print(x)
