#Global Variables
print("============== 1 ===================")
x = "awesome"
def myFunc():
    print("Python is", x)

myFunc()

print("============== 1.1 ===================")
x1 = "awesome"

def myFunc1():
    x1 = "fantastic"
    print("Python is", x1)

myFunc1()
print("Python is ", x1)

#The global Keyword
print("============== 2 ===================")
def myFunc2():
    global x2
    x2 = "fantastic"

myFunc2()
print("Python is", x2)

print("============== 2.2 ===================")

x3 = "awesome"

def myFunc3():
    global x3
    x3 = "fantastic"
    print("Python is", x3)

myFunc3()
print("Python is",x3)