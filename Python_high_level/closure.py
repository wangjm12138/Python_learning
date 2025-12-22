def say_hello(name):
    print('hello world')

    def say(msg):
        nonlocal name
        name = "Jackie plus"
        print(f'{name} say: '+msg)

    return say

if __name__ == '__main__':

    sa = say_hello("Jackie")
    sa("hello")