def array_scan():
    return [int(elem) for elem in input().strip().split()]


def array_increment(array):
    for i in range(len(array)):
        array[i] += 1


def array_print(array):
    out = [str(elem) for elem in array]
    out = ' '.join(out)
    print(out)


if __name__ == '__main__':
    array = array_scan()
    array_increment(array)
    array_print(array)
