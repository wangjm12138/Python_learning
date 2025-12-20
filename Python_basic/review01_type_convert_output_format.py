# shortcut key: ctrl + shift + up/down.  Move current line up/down
# shortcut key: ctrl + alt + L. Formalize code
# shortcut key: ctrl + shift + I. Check official document
# shortcut key: shift + enter. Go to next line
# shortcut key: ctrl + shift + f. Search code in the project
# shortcut key: ctrl + Y. Delete code line

from decimal import Decimal

def operate():
    print(17%2)
    print(8**0.5)
    pow(8,1/3)
    print(17/2)
    print(17//2)

def accurate_number():
    num = 22.345
    print('%.2f' % num)
    print(Decimal(str(num)).quantize(Decimal('0.00'), rounding='ROUND_HALF_UP'))

def output_format2():
    """
        f-string
    :return:
    """
    my_name = 'Jackie'
    my_age = 34
    my_city = 'Xiamen'
    print(f'My name: {my_name}, age: {my_age + 1}, city: {my_city}')

def output_format():
    """
    :description:
        %s: string
        %d: sign decimal integer
        %f: float
        %c: char
        %u: unsigned decimal integer
        %o: octal integer
        %x: Hexadecimal integer(low case: 0x)
        %X: Hexadecimal integer(high case: 0X)
        %e: exponent decimal integer(low case: e)
        %E: exponent decimal integer(high case: E)
        %g: %f and %e abbreviated
        %G: %f and %E abbreviated
    :return:
    """
    name = "Jackie";prefix=0x12138;subfix='w';money = 1000000;cent=0.254;area=1e10;age=34
    print("My name:%s_%x_%c has %d$ and %.1f cent and my house reach %.1e square meters at the age of %u" % (name,prefix,subfix,money,cent,area,age))


def type_conversion():
    """
    :description:
        int(x[,base]) : x -> integer
        float(x) : x -> float
        str(x) : x -> string
        complex(real[,imag]) : create complex, real, imag
        repr(x) : x -> python expression
        eval(str): str is python expression and return object
        tuple(x) : x -> tuple
        list(x) : x -> list
    :return:none
    """
    age_str = input('input age: ')
    print('Your age type', type(age_str))
    age = int(age_str)
    print('After conversion age type', type(age))


if __name__ == '__main__':
    # type_conversion()
    # output_format()
    # accurate_number()
    # output_format2()
    operate()
