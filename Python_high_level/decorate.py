class MyDecorate(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("hello", end=" ")
        return self.func(*args, **kwargs)

def decorate(func):

    def wrapper(*args, **kwargs):
        print("hello", end=" ")
        return func(*args, **kwargs)
    return wrapper

def say_hello():
    print("world 1")

@decorate
def say_hello2():
    print("world 2")

@MyDecorate
def say_hello3():
    print("world 3")

if __name__ == "__main__":
    enhance_say_hello = decorate(say_hello)
    enhance_say_hello()
    say_hello2()
    say_hello3()