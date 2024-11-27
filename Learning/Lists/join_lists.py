#Join Two Lists that using "+" Operator
print("============== 1 ===================")
joinList1 = ["a", "b","c"]
joinList2 = [1, 2, 3]
print(joinList1 + joinList2)

#appending that append() method
print("============== 1.1 ===================")
for jx in joinList2:
    joinList1.append(jx)
print(joinList1)

print("============== 1.2 ===================")
#you can use the extend() method
joinExtendList1 = ["a", "b","c"]
joinExtendList2 = [1, 2, 3]

joinExtendList1.extend(joinExtendList2)
print(joinExtendList1)