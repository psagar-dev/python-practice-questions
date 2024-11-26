#Loop Through a List
print("============== 1 ===================")
forItems = ["apple", "banana", "cherry"]
for x in forItems:
    print(x)

#Loop Through the Index Numbers
print("============== 2 ===================")
rangeItems = ["apple", "banana", "cherry"]
for i in range(len(rangeItems)):
    print(rangeItems[i])

#Using a While Loop
print("============== 3 ===================")
whileLoop = ["apple", "banana", "cherry"]
i = 0
while(i < len(whileLoop)):
    print(whileLoop[i])
    i = i + 1

#Looping Using List Comprehension (shortest syntax for looping through lists)
print("============== 4 ===================")
comprehensionLoop = ["apple", "banana", "cherry"]
[print(ix) for ix in comprehensionLoop]
