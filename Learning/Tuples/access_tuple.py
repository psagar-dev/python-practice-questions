#Access Tuple Items
print("============== 1 ===================")
#Print the second item in the tuple:
accessItems = ("Apple", "Banana", "Cherry")
print(accessItems[1])

#Negative Indexing
print("============== 2 ===================")
#Print the last item of the tuple
print(accessItems[-1])

#Range of Indexes
print("============== 3 ===================")
rangeOfIndex = ("Apple", "Banana", "Cherry", "orange", "Kiwi", "Melon", "Mengo")
#Return the third, fourth, and fifth item:
print(rangeOfIndex[2:5])

print("============== 3.1 ===================")
#This example returns the items from the beginning to, but NOT included, "kiwi":
print(rangeOfIndex[:4])

print("============== 3.2 ===================")
#This example returns the items from "cherry" and to the end:
print(rangeOfIndex[2:])

#Range of Negative Indexes
print("============== 4 ===================")
#This example returns the items from index -4 (included) to index -1 (excluded)
print(rangeOfIndex[-4:-1])

#Check if Item Exists
print("============== 5 ===================")
if "Apple" in rangeOfIndex:
    print("Yes, 'Apple' is in the fruits tuple")