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

#endswith() that Returns true if the string ends with the specified value
print("============== 6 ===================")
endswithText = "Hello, welcome to my world."
print(endswithText.endswith("my world."))
print(endswithText.endswith("my world.", 5, 11))
print(endswithText.endswith(("castle.","world.")))

#expandtabs() Sets the tab size of the string
print("============== 7 ===================")
expandtabsText = "H\te\tl\tl\to"
print(expandtabsText)
print(expandtabsText.expandtabs())
print(expandtabsText.expandtabs(2))
print(expandtabsText.expandtabs(4))
print(expandtabsText.expandtabs(10))

#find() that Searches the string for a specified value and returns the position of where it was found
print("============== 8 ===================")
findText = "Hello, welcome to my world."
print(findText.find("welcome"))
print(findText.find("e"))
print(findText.find("e",5,10))

#format() that Formats specified values in a string
print("============== 9 ===================")
formatText = "For only {price:.2f} dollars!"
print(formatText.format(price = 49))
print("My name is {fname}, I'm {age}".format(fname = "Sagar",age = 30))


#index() that Searches the string for a specified value and returns the position of where it was found
print("============== 10 ===================")
indexText = "Hello, welcome to my world."
print(indexText.index("welcome"))
print(indexText.index("e"))
print(indexText.index("e",5,10))