
"""
    container: 1. sequence: list, string, tuple 2. mapping: dict 3. Set
"""
def set_operation():
    set1 = {1, 2, 3}
    print(set1)
    # only support immutable/hashable object
    # immutable object: string, int, float, tuple
    # mutable object: list , dict, set
    set2 = {4, 5, 6,[100,200]}
    print(set2) #report error

def dic_operation():
    dic1 = {"a":1, "b":2, "c":3}
    print(dic1)
    dic2 = dict(name='ls', age=53, city='beijing')
    print(dic2)
    dic3 = dict([('name', 'zs'),('age', 44), ('city', 'beijing'), ('high',18)])
    del dic3['name']
    print(dic3)
    for key, value in dic3.items():
        print(f'key:{key}, value:{value}')

def sequence_operation():
    lst = [100]
    lst += [1,2,3]
    print(lst)
    lst *= 2
    print(lst)

def tuple_operation():
    tuple1 = (1, 2, 3)
    print(tuple1)
    print(tuple1.index(2))
    print(tuple1.count(2))

def list_operation():
    list1 = [1, 2, 2,3, 4]
    print(list1.index(3))
    print(list1.count(3))
    list1.append(5)
    print(list1)
    list1.extend([6, 7, 8])
    print(list1)
    list1.pop()
    print(list1)
    print(list1[::-1])
    list1.reverse()
    print(list1)
    list1.sort()
    print(list1)


def string_operation():
    str1 = "abcdefg"
    str2=str1[2:5]
    print(str2)
    print(str1.find('cde', 2, 6))
    str3 = "abc def ghi"
    print(str3.split(" "))
    print(str3.partition(" "))


if __name__ == '__main__':
    # string_operation()
    # list_operation()
    # tuple_operation()
    # sequence_operation()
    # dic_operation()
    set_operation()