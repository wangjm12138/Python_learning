class A:
    def __init__(self, x):
        self.x = x

class UpperMetaClass2(type):
    def __new__(cls, class_name, class_parents, new_atts):
        new_atts = dict((name, value) if name.startswith('_') else(name.upper(),value) for name, value in new_atts.items())
        return super().__new__(cls, class_name, class_parents, new_atts)

def UpperMetaClass(class_name, class_parents, class_attrs):
    new_atts = {}
    for name, value in class_attrs.items():
        if not name.startswith('_'):
            print(name, value)
            new_atts[name.upper()] = value
        else:
            new_atts[name] = value
    return type(class_name,class_parents,new_atts)

class Person(object, metaclass=UpperMetaClass):
    name = 'zhangsan'

class Person2(object, metaclass=UpperMetaClass2):
    name = 'zhangsan'

if __name__ == '__main__':
    a = A(5)
    print(a.__class__)
    print(A.__bases__)

    print(int.__bases__) #int的父类
    print(int.__class__) #int是由哪个类创建的


    print(object.__class__)


    # c2 = type('Person',(object,),{'age':33})
    print(hasattr(Person, 'name'))
    print(hasattr(Person, 'NAME'))
    print(hasattr(Person2, 'name'))
    print(hasattr(Person2, 'NAME'))