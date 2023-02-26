# Sets: unordered, mutable, no duplicates
# myset = set()

# myset.add(1)
# myset.add(2)
# myset.add(3)

# myset.remove(4)
# myset.discard(4)
# myset.clear()

# print(myset.pop())
# print(myset.pop())
# print(myset)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

print(setA)
print(setB)

# setA.intersection_update(setB)
# print(setA)

# setA.difference_update(setB)
# print(setA)

setA.symmetric_difference_update(setB)
print(setA)