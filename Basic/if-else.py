#if statement
print("============== 1 ===================")
ifa = 33
ifb = 200
if ifb > ifa:
    print("b is greater than a")

#Elif
print("============== 2 ===================")
elseIfa = 33
elseIfb = 33
if elseIfb > elseIfa:
    print("`elseIfb` is Greater then `elseIfb`")
elif elseIfa == elseIfb:
    print("`elseIfb` and `elseIfb` are equal")

#Else
print("============== 3 ===================")
elIfa = 200
elIfb = 33
if elIfb > elIfa:
    print("`elIfb` is greater then `elIfa`")
elif elIfb == elIfa:
    print("`elIfb` and `elIfa` is equal")
else:
    print("elIfa is greater then `elIfb`")

#Short Hand If
print("============== 4 ===================")
shifa = 250
shifb = 40
if shifa > shifb: print("`shifa` is greater then `shifb`")

#Short Hand If ... Else
print("============== 4 ===================")
shifela = 40
shifelb = 200
print("`shifela` is greater then `shifelb`") if shifela > shifelb else print("`shifelb` is greate then `shifela`")

print("============== 4.1 ===================")
shifelsa = 330
shifelsb = 330

print("`shifelsa` is greater then `shifelsb`") if shifelsa > shifelsb else print("shifelsb and shifelsa are equal") if shifelsa == shifelsb else print("`shifelsb` is greate then `shifelsa`")

#And
print("============== 4 ===================")
anda = 200
andb = 33
andc = 500
if anda > andb and andc > anda:
    print("Both condition are true")

#OR
print("============== 5 ===================")
ora = 200
orb = 33
orc = 500

if ora > orb or ora > orc:
    print("At least one of the conditions is True")

#Not
print("============== 6 ===================")
nota = 40
notb = 200
if not nota > notb:
    print("nota is NOT greater than notb")

#Nested If
print("============== 7 ===================")
nestedIfx = 41
if nestedIfx > 10:
    print("Above ten,")
    if nestedIfx > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#The pass Statement
print("============== 8 ===================")

if 200 > 33:
    pass