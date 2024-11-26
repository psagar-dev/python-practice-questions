#List
print("============== 1 ===================")
thisList = ["apple","banana","cherry"]
print(thisList)

#Allow Duplicates
print("============== 2 ===================")
ad = ["apple", "banana", "cherry", "apple", "cherry"]
print(ad)

#List Length
print("============== 3 ===================")
listLength = ["apple", "banana", "cherry"]
print(len(listLength))

#List Items - Data Types
print("============== 4 ===================")
listString = ["apple", "banana", "cherry"]
listInt = [1, 5, 7, 9, 3]
listBoolean = [True, False, False]
print(listString)
print(listInt)
print(listBoolean)

#A list can contain different data types:
print("============== 5 ===================")
listDifferentDataTypes = ["abc", 34, True, 40, "male"]
print(listDifferentDataTypes)

#type()
print("============== 6 ===================")
listDataType = ["apple", "banana", "cherry"]
print(type(listDataType))

#The list() Constructor
print("============== 7 ===================")
listConstructor = list(("apple", "banana", "cherry"))
print(listConstructor)