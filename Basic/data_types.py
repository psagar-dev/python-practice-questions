#Text Type
print("============== 1 ===================")
textType = "Hello, World!"
print(textType, type(textType))

#Numeric Types
print("============== 2 ===================")
#int
numericTypeInt = 20
print(numericTypeInt, type(numericTypeInt))

#float
print("============== 2.1 ===================")
numericTypeFloat = 20.5
print(numericTypeFloat, type(numericTypeFloat))

#complex
print("============== 2.2 ===================")
numericTypeComplex = 1j
print(numericTypeComplex, type(numericTypeComplex))

#Sequence Types
print("============== 3 ===================")
#list
sequenceTypeList = ["Apple", "Banana", "Orange"]
print(sequenceTypeList, type(sequenceTypeList))

#tuple
print("============== 3.1 ===================")
sequenceTypeTuple = ("Apple", "Banana", "Orange")
print(sequenceTypeTuple, type(sequenceTypeTuple))

#range
print("============== 3.2 ===================")
sequenceTypeRange = range(1,10)
print(sequenceTypeRange, type(sequenceTypeRange))

#Mapping Type (Dict)
print("============== 4 ===================")
mappingTypeDict = {"name": "John","age": 59}
print(mappingTypeDict, type(mappingTypeDict))

#Set Types
print("============== 5 ===================")
#Set
setTypeSet =  {"Apple", "Banana", "Cherry"}
print(setTypeSet, type(setTypeSet))

#frozenset
print("============== 5.1 ===================")
setTypeFrozenSet = frozenset({"Apple", "Banana", "Cherry"})
print(setTypeFrozenSet, type(setTypeFrozenSet))

#Boolean Type
print("============== 6 ===================")
booleanType = True
print(booleanType, type(booleanType))

#Binary Types
print("============== 7 ===================")
#bytes
bineryTypesBytes = b"Hello"
print(bineryTypesBytes, type(bineryTypesBytes))

#bytearray
print("============== 7.1 ===================")
bineryTypesByteArray = bytearray(5)
print(bineryTypesByteArray, type(bineryTypesByteArray))

#memoryview
print("============== 7.1 ===================")
bineryTypesMemoryView = memoryview(bytes(5))
print(bineryTypesMemoryView, type(bineryTypesMemoryView))

#None Type
print("============== 8 ===================")
noneType = None
print(noneType, type(noneType))