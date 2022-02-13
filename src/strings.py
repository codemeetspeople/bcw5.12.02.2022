if __name__ == '__main__':  # pragma: no cover
    # x, y = list(map(int, input().strip().split()))
    #
    # print('%d + %d = %d' % (x, y, x+y))
    # print('{} - {} = {}'.format(x, y, x-y))
    # print('{x} * {y} = {result}'.format(x=x, y=y, result=x*y))
    # print(f'{x} / {y} = {x / y}')

    params = {
        'male': 'John',
        'female': 'Jane'
    }

    print('%(male)s + %(female)s = love' % params)
    print('{male} + {female} = love'.format(**params))
    print(f'{params["male"]} + {params["female"]} = love')
