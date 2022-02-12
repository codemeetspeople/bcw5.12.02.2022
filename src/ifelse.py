if __name__ == '__main__':
    data = input()
    data.strip()

    data = data.split()
    data = list(map(int, data))

    x, y = data

    if x <= y:
        print('alpha')
    elif x < 0:
        print('bravo')
    elif y == 0:
        print('charlie')
    else:
        print('zulu')
