# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
# from collections import Counter
# a = "aaaaabbbbccc"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# 
# d = {'a':1, 'b':2}
# print(d.items())
# print(d.keys())
# print(d.values())

# print(my_counter.most_common(1))
# print(my_counter.most_common(1)[0])
# print(my_counter.most_common(1)[0][0])
# 
# print(my_counter.elements())
# print(list(my_counter.elements()))

# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(1, -4)
# print(pt)
# print(pt.x, pt.y)

# from collections import OrderedDict
# # ordered_dict = OrderedDict()
# ordered_dict = {}
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# ordered_dict['a'] = 1
# print(ordered_dict)

# from collections import defaultdict
# d = defaultdict(list)
# d['a'] = 1
# d['b'] = 2
# print(d)
# print(d['a'])
# print(d['b'])
# print(d['c'])

from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend([4, 5, 6])
print(d)

d.extendleft([1, 2, 3])
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)
