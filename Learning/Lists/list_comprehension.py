#List Comprehension
print("============== 1 ===================")
#Without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for fx in fruits:
    if 'a' in fx:
        newlist.append(fx)
print(newlist)
#With list comprehension
print([wfx for wfx in fruits if "a" in wfx])