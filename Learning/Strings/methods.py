#capitalize() That Converts the first character to upper case
print("============== 1 ===================")
capitalizeText = "hello, and welcome to my world."
print(capitalizeText.capitalize())

print("============== 1.1 ===================")
capitalizeText1 = "python is FUN!"
print(capitalizeText1.capitalize())

print("============== 1.2 ===================")
capitalizeText2 = "36 python is FUN!"
print(capitalizeText2.capitalize())

#casefold that Converts string into lower case
print("============== 2 ===================")
casefoldText = "Hello, And Welcome To My World!"
print(casefoldText.casefold())


#center() that Returns a centered string
print("============== 3 ===================")
centerText = "Banana"
print(centerText.center(30))

print("============== 3.1 ===================")
centerText = "Banana"
print(centerText.center(30, "0"))


#count() that Returns the number of times a specified value occurs in a string
print("============== 4 ===================")
countText = "I love apples, apple are my favorite fruit apple"
print(countText.count("apple"))
print(countText.count('apple', 10,20))

#encode() that Returns an encoded version of the string
print("============== 5 ===================")
encodeText = "My name is Ståle"
print(encodeText.encode())
