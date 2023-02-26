# Strings: ordered, immutable, text representation
"""
from timeit import default_timer as timer
my_list = ['a'] * 6
print(my_list)

# bad
start = timer()
my_string = ''
for i in my_list:
    my_string += i
print(my_string)
stop = timer()
print(stop - start)

# good
start = timer()
my_string = ''.join(my_list)
print(my_string)
stop = timer()
print(stop - start)
"""
# %
# var = "Tom"
# my_string = "the variable is %s" % var
# print(my_string)
# 
# var = 3.123456789
# my_string = "the variable is %.2f" % var
# print(my_string)

# .format()
# var1 = 3.123456789
# var2 = 6
# my_string = "the variable is {:.2f} and {}".format(var1, var2)
# print(my_string)

# f-String
var1 = 3.123456789
var2 = 6
my_string = f"the variable is {var1*2:.2f} and {var2}"
print(my_string)

