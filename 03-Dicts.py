# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = mydict["name"]
print(value)

mydict["email"] = "max@xyz.com"
print(mydict)

mydict["email"] = "coolmax@xyz.com"
print(mydict)

# del mydict["name"]
# print(mydict)

# mydict.pop("age")
# print(mydict)

# mydict.popitem()
# print(mydict)

# try:
#     print(mydict["town"])
# except:
#     print("Error")

# for key in mydict:
#     print(key)
#     
# for key in mydict.keys():
#     print(key)
#
# for value in mydict.values():
#     print(value)

for key, value in mydict.items():
    print(key, value)