# def mygenerator():
#     yield 3
#     yield 1
#     yield 2
#
# g = mygenerator()
#
# # print(sum(g))
#
# print(sorted(g))

# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -= 1
#
# cd = countdown(4)
#
# value = next(cd)
# print(value)
#
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))

#import sys
#
#def firstn(n):
#    nums = []
#    num = 0
#    while num < n:
#        nums.append(num)
#        num += 1
#    return nums
#
# mylist = firstn(10)
# print(mylist)
#
# print(sum(firstn(10)))
#
# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
# print(sum(firstn_generator(10)))
#
# print(sys.getsizeof(firstn(10)))
# print(sys.getsizeof(firstn_generator(10)))

# def fibonacci(limit):
#     # 0 1 1 2 3 5 8 13 ...
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b
# 
# fib = fibonacci(30)
# 
# for i in fib:
#     print(i)

import sys

mygenerator = (i for i in range(10) if i % 2 == 0)
print(sys.getsizeof(mygenerator))
for i in mygenerator:
    print(i)

mylistcomph = [i for i in range(10) if i % 2 == 0]
print(sys.getsizeof(mylistcomph))
print(mylistcomph)
