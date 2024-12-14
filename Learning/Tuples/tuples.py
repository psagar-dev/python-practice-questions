#Python Tuples
print("============== 1 ===================")
createTuple = ("Apple", "Banana", "Cherry")
print("Create Tuple"," ==> ", createTuple)

#Tuple Items
print(createTuple[0], createTuple[1])

#Allow Duplicates
print("============== 2 ===================")
allowDublicate = ("Apple", "Banana", "Cherry", "Apple")
print(allowDublicate)

#Tuple Length
print("============== 3 ===================")
lenTuple = ("Apple", "Banana", "Cherry", "Apple")
print('Tuple Length'," ==> ", len(lenTuple))

#Create Tuple With One Item
print("============== 4 ===================")
tupleOneItemWithComma = ("Apple",)
print("Tuple With One Item "," ==> ",type(tupleOneItemWithComma))

tupleOneItemWithoutComma = ("Apple")
print("Tuple with one item Without comma "," ==> ", type(tupleOneItemWithoutComma))

#Tuple Items - Data Types
print("============== 5 ===================")
dataTypeOfString = ("Apple", "Banana", "Cherry")
dataTypeOfNumber = (1,2,3,5)
dataTypeOfBoolean = (True, False, True, True)
dataTypeMix = ("Apple", True, 1, "Banana")

#The tuple() Constructor
print("============== 6 ===================")
tupleConstructor = tuple(("Apple", "Banana", "Cherry"))
print("tuple() Constructor", " ==> ",tupleConstructor)