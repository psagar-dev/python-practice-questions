#Sort List Alphanumerically
print("============== 1 ===================")
sortListAlphaNumericall = ["orange", "mango", "kiwi", "pineapple", "banana"]
sortListAlphaNumericall.sort()
print(sortListAlphaNumericall)

#Sort the list numerically
print("============== 2 ===================")
sortListNumerically = [100, 50, 65, 82, 23]
sortListNumerically.sort()
print(sortListNumerically)

#SortDescending
print("============== 3 ===================")
sortListAlphaNumericall.sort(reverse=True)
sortListNumerically.sort(reverse=True)
print(sortListNumerically)
print(sortListNumerically)

#Case Insensitive Sort
print("============== 4 ===================")
caseInsensitiveSort = ["banana", "Orange", "Kiwi", "cherry"]
caseInsensitiveSort.sort()
print(caseInsensitiveSort)
caseInsensitiveSort.sort(key=str.lower)
print(caseInsensitiveSort)

#Reverse Order
print("============== 5 ===================")
reverseOrder = ["banana", "Orange", "Kiwi", "cherry"]
reverseOrder.reverse()
print(reverseOrder)