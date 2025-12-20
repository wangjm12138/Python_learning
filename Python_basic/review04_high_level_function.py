from functools import reduce


def sum_num(a, b, f):
    """

    :param a:
    :param b:
    :param f: high level function
    :return:
    """
    return f(a) + f(b)


def sum_num2(*args):
    def _sum_nums():
        sum1 = 0
        for num in args:
            sum1 += num
        return sum1
    return _sum_nums

def high_level_function():
    print(sum_num(1, 2, abs))
    print(sum_num(1, 2, lambda n: n**2))
    print(sum_num2(1,2,3,4)())


def inner_function():
    print(list(map(lambda item: item + 1, [1, 2, 3, 4],)))
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
    lst = [1, 3, 2, 4]
    ret = filter(lambda num: num % 2 == 0, lst)
    print(list(ret))
    print(lst)
    ret_sort = sorted(lst, key=lambda num: num, reverse=True)
    print(ret_sort)
    print(lst)

if __name__ == '__main__':
    high_level_function()
    inner_function()