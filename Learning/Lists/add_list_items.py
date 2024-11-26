#Append Items
print("============== 1 ===================")
appendList = ["apple", "banana", "cherry"]
appendList.append("orange")
print(appendList)

#Insert Items
print("============== 2 ===================")
insertItems = ["apple", "banana", "cherry"]
insertItems.insert(1, "orange")
print(insertItems)

#Extend List
print("============== 3 ===================")
extendList1 = ["apple", "banana", "cherry"]
extendList1 = ["mango", "pineapple", "papaya"]
extendList1.extend(extendList1)
print(extendList1)

#Add Any Iterable
print("============== 4 ===================")
addanyIterable = ["apple", "banana", "cherry"]
addanyIterableTuple = ("kiwi", "orange")
addanyIterable.extend(addanyIterableTuple)
print(addanyIterable)