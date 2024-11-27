#Use the copy() method
print("============== 1 ===================")
useCopyList = ["apple", "banana", "cherry"]
myUseCopyList = useCopyList.copy()
print(myUseCopyList)

#Use the list() method that Another way to make a copy is to use the built-in method list().
print("============== 2 ===================")
listCopy = ["apple", "banana", "cherry"]
myListCopy = list(listCopy)
print(myListCopy)

#Use the slice Operator that You can also make a copy of a list by using the : (slice) operator.
print("============== 3 ===================")
copySliceOperator = ["apple", "banana", "cherry"]
myCopySliceOperator = copySliceOperator[:]
print(myCopySliceOperator)