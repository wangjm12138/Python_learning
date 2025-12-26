class MyClass(object):

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

if __name__ == "__main__":
    myclass = MyClass(2)
    print(myclass.age)
    myclass.age = 10
    print(myclass.age)
    myclass.age = 20
    print(myclass.age)