import random

a = random.random()
a = random.uniform(1, 10)
a = random.randint(1, 10)
a = random.randrange(1, 10)
a = random.normalvariate(0, 1)
print(a)

mylist = list("ABCDEFGH")
a = random.choice(mylist)
print(a)