class Employee:
    def __init__(self, name, gender, age, mobile_number, is_leave):
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile_number = mobile_number
        self.is_leave = is_leave

    def __str__(self):
        return f'{self.name}\t{self.gender}\t{self.age}\t{self.mobile_number}\t{self.is_leave}'


if __name__ == '__main__':
    e = Employee('John', 'Male', 42, "1822222", True)
    print(e.__dict__)
    print(vars(e))