#Remove Specified Item
print("============== 1 ===================")
removeSpecifiedItem = ["apple", "banana", "cherry"]
removeSpecifiedItem.remove("banana")
print(removeSpecifiedItem)

#more than one item when using remove() method that remove first
print("============== 2 ===================")
moreThanOneRemoveItems = ["apple", "banana", "cherry", "banana", "kiwi"]
moreThanOneRemoveItems.remove("banana")
print(moreThanOneRemoveItems)

#Remove Specified Index using pop()
print("============== 3 ===================")
removeSpecifiedIndexList = ["apple", "banana", "cherry"]
removeSpecifiedIndexList.pop(1)
print(removeSpecifiedIndexList)

#if you do not specify the index, the pop() method removes the last item.
print("============== 4 ===================")
removeNotSpecifiedIndexList = ["apple", "banana", "cherry"]
removeNotSpecifiedIndexList.pop()
print(removeNotSpecifiedIndexList)

#del keyword removes the specified index
print("============== 5 ===================")
delSpecifiedIndex = ["apple", "banana", "cherry"]
del delSpecifiedIndex[1]
print(delSpecifiedIndex)

#The del keyword can also delete the list completely.
# thislist = ["apple", "banana", "cherry"]
# del thislist

#Clear the List (The clear() method empties the list)
print("============== 6 ===================")
clearTheList = ["apple", "banana", "cherry"]
clearTheList.clear()
print(clearTheList)