#The while Loop
print("============== 1 ===================")
i = 1
while i < 6:
    print(i)
    i += 1

#The break Statement
print("============== 2 ===================")
breaki = 1
while breaki < 6:
    print(breaki)
    if breaki == 3:
        break
    breaki += 1

#The continue Statement
print("============== 3 ===================")
continuei = 0
while continuei < 6:
    continuei += 1
    if(continuei == 3):
        continue

    print(continuei)

#The else Statement
print("============== 4 ===================")
elsei = 1
while elsei < 6:
    print(elsei)
    elsei += 1
else:
    print("`elsei` is no longer less than 6")
