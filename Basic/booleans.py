#Boolean Values
print("============== 1 ===================")
print(10 > 9)
print(10 == 9)
print(10 < 9)
if(33 > 200):
    print("b is greter than a")
else:
    print("B is not greter than a")

#Evaluate Values and Variables
print("============== 2 ===================")
print(bool("Hello"))
print(bool(15))

#Most Values are True
print("============== 3 ===================")
print(bool("abc"))
print(bool(123))
print(bool(["Apple", "cherry", "banana"]))

#Some Values are False
print("============== 4 ===================")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myClass():
    def __len__(self):
        return 0
    
myObj = myClass()
print(bool(myObj))

#Functions can Return a Boolean
print("============== 5 ===================")
def myFunction():
    return True

print(myFunction())

print(isinstance(200, int))
print(isinstance("Hello", str))
print(isinstance("True", bool))