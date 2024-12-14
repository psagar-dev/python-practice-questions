#Unpacking a Tuple
print("============== 1 ===================")
fruits = ("Apple", "Banana", "Cherry")

(green , yellow, red) = fruits

print(green, yellow, red)

print("============== 2 ===================")
#Using Asterisk*
asteriskFruits = ("Apple", "Banana", "Cherry", "strawberry", "raspberry")

print("============== 3 ===================")
#Assign the rest of the values as a list called "red":
(green, yellow, *red) = asteriskFruits
print(green, yellow, red)

print("============== 4 ===================")
#Add a list of values the "tropic" variable:
(green, *tropic, red) = asteriskFruits
print(green, tropic, red)