def generator():
    v1 = yield 1
    print(f'first time value:{v1}')
    v2 = yield 2
    print(f'second time value:{v2}')
    v3 = yield 3
    print(f'third time value:{v3}')
    v4 = yield 4
    print(f'fourth time value:{v4}')

def generator_func():
    i = 2
    yield i
    while True:
        i +=1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i



if __name__ == '__main__':
    g = generator()
    print(hasattr(g, '__iter__'))
    print(hasattr(g, '__next__'))
    print(next(g))
    print(g.send(100))
    print(g.send(200))

    g2 = generator_func()
    num = next(g2)
    while num <= 100:
        print(num)
        num = next(g2)
