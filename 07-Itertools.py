# itertools: product, permutations, combinations, accumulate, groupby, and infinite itertools
# from itertools import product
# a = [1, 2]
# b = [3, 4]
# prod = product(a, b)
# print(prod)
# print(list(prod))
# 
# a = [1, 2]
# b = [3]
# prod = product(a, b, repeat=2)
# print(list(prod))

# from itertools import permutations
# a = [1, 2, 3]
# perm = permutations(a)
# print(list(perm))
# 
# perm = permutations(a, 2)
# print(list(perm))

# from itertools import combinations, combinations_with_replacement
# a = [1, 2, 3, 4]
# comb = combinations(a, 2)
# print(list(comb))
# comb_repl = combinations_with_replacement(a, 2)
# print(list(comb_repl))

# from itertools import accumulate
# import operator
# a = [1, 2, 5, 3, 4]
# acc = accumulate(a)
# print(a)
# print(list(acc))
# 
# acc = accumulate(a, func=operator.mul)
# print(a)
# print(list(acc))
# 
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))

# from itertools import groupby
# 
# def smaller_than_3(x):
#     return x < 3
# 
# a = [1, 2, 3, 4]
# # group_obj = groupby(a, key=smaller_than_3)
# group_obj = groupby(a, key=lambda x: x < 3)
# for key, value in group_obj:
#     print(key, list(value))
# 
# persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
#            {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
# group_obj = groupby(persons, key=lambda x: x['age'])
# for key, value in group_obj:
#     print(key, list(value))

from itertools import count, cycle, repeat

# for i in count(10):
#     print(i)
#     if i == 15:
#         break

# a = [1, 2, 3]
# for i in cycle(a):
#     print(i)

for i in repeat(1, 5):
    print(i)





