# Lists: ordered, mutable, allows duplicate elements
mylist  = ["banana", "cherry", "apple"]
print(mylist)

mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("cherry")
print(item)
print(mylist)

new_list = sorted(mylist)
print(mylist)
print(new_list)