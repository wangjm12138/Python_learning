from typing import Iterator


class MyIterator(object):
    def __init__(self, stop_num):
        self.stop_num = stop_num
        self.num = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        if self.num == self.stop_num:
            print("end")
            self.num = -1
            raise StopIteration
        return self.num

class MyIterator2(object):
    def __init__(self, stop_num):
        MyIterator(5)

if __name__ == '__main__':
    obj = MyIterator(5)
    print(isinstance(obj, Iterator))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))

    for num in obj:
        print(num)
    obj2 = MyIterator(5)
    for num in obj2:
        print(num)