#Python Numbers
print("============== 1 ===================")
#Int
intNumber = 1
intNumber2 = 12345678901112
intNumber3 = -202352
print(intNumber, type(intNumber))
print(intNumber2, type(intNumber2))
print(intNumber3, type(intNumber3))

#Float
print("============== 2 ===================")
floatNumber = 20.5
floatNumber2 = 1.0
floatNumber3 = -35.59
floatNumber4 = 35e3
floatNumber5 = 12E4
floatNumber6 = -87.7e100

print(floatNumber, type(floatNumber))
print(floatNumber2, type(floatNumber2))
print(floatNumber3, type(floatNumber3))
print(floatNumber4, type(floatNumber4))
print(floatNumber5, type(floatNumber5))
print(floatNumber6, type(floatNumber6))

#Complex
print("============== 3 ===================")
complexNumber = 3+5j
complexNumber1 = 5j
complexNumber2 = -5j

print(complexNumber, type(complexNumber))
print(complexNumber1, type(complexNumber1))
print(complexNumber2, type(complexNumber2))

#Type Conversion
print("============== 4 ===================")
typeConvertInt = 1
typeConvertFloat = 2.2
typeConvertComplex = 3j

print(typeConvertInt, float(typeConvertInt))
print(typeConvertFloat, int(typeConvertFloat))
print(typeConvertComplex, complex(typeConvertInt))

#Random Number
print("============== 5 ===================")
import random

print(random.randrange(1,100))