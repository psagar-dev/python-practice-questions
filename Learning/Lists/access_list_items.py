#Access Items
print("============== 1 ===================")
accessItems = ["apple", "banana", "cherry"]
print(accessItems[1])

#Negative Indexing
print("============== 2 ===================")
negativeIndexing = ["apple", "banana", "cherry"]
print(negativeIndexing[-1])

#Range of Indexes
print("============== 3 ===================")
rangeOfIndexes = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(rangeOfIndexes[2:5])
print(rangeOfIndexes[:5])
print(rangeOfIndexes[2:])

#Range of Negative Indexes
print("============== 4 ===================")
rangeOfNegativeIndexes = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(rangeOfNegativeIndexes[-4:-2])

#Check if Item Exists
print("============== 5 ===================")
listItemExists = ["apple", "banana", "cherry"]
if "apple" in listItemExists:
    print("Yes, 'apple' is in the fruits list")