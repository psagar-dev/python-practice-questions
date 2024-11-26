#Change Item Value
print("============== 1 ===================")
changeItemList = ["apple", "banana", "cherry"]
changeItemList[1] = "blackcurrant"
print(changeItemList)

#Change a Range of Item Values
print("============== 2 ===================")
changeRangeOfItemList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
changeRangeOfItemList[1:3] = ["blackcurrant", "watermelon"]
print(changeRangeOfItemList)

#Replace & new add Items
print("============== 3 ===================")
replaceNewAddItems = ["apple", "banana", "cherry"]
replaceNewAddItems[1:2] = ["blackcurrant", "watermelon"]
print(replaceNewAddItems)

#insertLessItemsReplace
print("============== 3 ===================")
insertLessItems = ["apple", "banana", "cherry"]
insertLessItems[1:3] = ["watermelon"]
print(insertLessItems)

#Insert Items
print("============== 4 ===================")
insertItems = ["apple", "banana", "cherry"]
insertItems.insert(1,"watermelon")
print(insertItems)