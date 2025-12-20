
class Parent2:
    def __init__(self,a):
        print("Parent2 constructor")

class Parent:
    def __init__(self, a):
        print("Parent constructor")
        super().__init__(a) #if add this sentence, will call nex MRO,  Parent2 __init__
        self.a = a

    def run(self):
        print("Parent run")

    def __private_run(self):
        print("Parent __p_run"+ str(self.a))

class Example (Parent,Parent2):
    A = 100
    def __init__(self, a):
        print("init example")
        super().__init__(a)
        self.__a = a

    def __str__(self):
        return str(f'example instance a: {self.a}, class A: {self.A}')

    def __new__(cls, *args, **kwargs):
        print("__new__")
        return object.__new__(cls)

    def run(self):
        print("running example"+str(self.a))
        super().run()

    @classmethod
    def work(cls):
        print("only can call cls.A: "+str(cls.A) + " cannot call cls.a")

    @staticmethod
    def work2():
        print("cannot call self.a or cls.A")

    def __del__(self):
        print("deleting example"+str(self.a))

def class_practice():
    example = Example(1)
    print(isinstance(example,Example))
    print(isinstance(example,Parent))
    print(issubclass(Example,Parent))
    print(example.a)
    print(Example.A)
    Example.A = 200
    print(example.A)
    example.A = 300
    print(Example.A) #200， exmaple.A will create A property to this instance
    print(example.A)
    print(Example.__mro__)
    example.run()
    example.work()
    Example.work()
    example.work2()
    Example.work2()
    print(example)

    del example

if __name__ == '__main__':
    class_practice()