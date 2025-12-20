import traceback

class MyException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyException: {self.value}"

def my_function():
    raise MyException("This is my exception")

try:
    my_function()
except Exception:
    print(traceback.format_exc())
finally:
    print("finally")