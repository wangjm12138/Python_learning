import math
# import math as m
# from math import sqrt
# from math import sqrt as sq
# from math import *

print(math.log2(8))

import sys
print(sys.path) # find module from this path


from my_module import *
print(my_sum(1,2))
# print(test(1,2))  #cannot use test as __all__ only define my_sum

# but if you use this way , it can use my_sum and test
# import my_module
# print(my_module.my_sum(1,2))
# print(my_module.test(1,2))

from my_package import my_module2
print(my_module2.__name__)
print(my_module2.my_sum(1,2))

