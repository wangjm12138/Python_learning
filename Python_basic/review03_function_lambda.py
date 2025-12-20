

def function_operation(a:int, b:int, c:int):
    return a + b + c

def function_operation2(a=1, *agrs):
    for x in agrs:
        a +=x
    return a

def function_operation3(c=1, **kwargs):
    for k, v in kwargs.items():
        c += v
    return c

def function_operation4(a, lst=[1, 2]):
    """
    :param a:
    :param lst: mutable list
    :return:
    """
    if a not in lst:
        lst.append(a)
    return lst

def test(n: int) -> int:
    if n == 1:
        return 1
    return n * test(n - 1)

def lambda_practice():
    fn1 = lambda a, b: a + b
    print(fn1(1,2))
    lst = [
        {'a': 3, 'b': 2},
        {'a': 1, 'b': 4},
        {'a': 2, 'b': 6},
    ]
    lst.sort(key=lambda x: x['a'])
    print(lst)
    fn2 = lambda z=100, *args: z + sum(args)
    print(fn2(10,1,2,3,4))

if __name__ == '__main__':
    b1 = function_operation(1,2,3)
    print(b1)
    b2 = function_operation2(1,2,3,4)
    print(b2)
    b3 = function_operation3(a=1,b=2)
    print(b3)
    b4 = function_operation4(3)
    print(f'返回值：{b4}')
    b5 = function_operation4(5)
    print(f'返回值：{b5}') #1,2,3,5，as lst is mutable
    b6 = test(3)
    print(b6)
    lambda_practice()
