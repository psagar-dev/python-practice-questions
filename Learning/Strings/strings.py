# Strings in python are surrounded by either single quotation marks, or double quotation marks
print("Hello")
print('Hello')

#Quotes Inside Quotes
print("============== 1 ===================")
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny2"')

#Assign String to a Variable
print("=============== 2 ==================")
a = "Hello"
print(a)

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:
print("=============== 3 =================")
mls = """Lorem's ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(mls)

print("================ 4 =================")
smls = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(smls)

#Strings are Arrays
print("================ 5 =================")
sa = "Hello, World!"
print(sa[1])
print("================ 6 ===============")

#Looping Through a String
print("================= 7 ================")
for x in "banana":
    print(x)

#String Length
print("================= 8 ================")
print(f"String Length: {len("Hello, World!")}")

#Check String
print("================= 9 ===============")
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes,'free' is present.")

#Check if NOT
print("================= 10 ================")
print("expensive" not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")