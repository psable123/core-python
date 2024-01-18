name = input("Enter your name ")
print("Hello ", name)

print("Hello {1} {0}" .format(234, name))

print(f"Hello {name}")

def sayhello(name):
    msg = "hello "
    msg = msg+name
    return msg


a = sayhello(name)
print(a)
print(f"Upper: {a.upper()}")
print(f"is upper: {a.isupper()}")
print(f"lower: {a.lower()}")
print(f"islower: {a.islower()}")
print(f"title: {a.title()}")
print(f"capitalize: {a.capitalize()}")
print(f"isspace: {a.isspace()}")
print(f"find: {a.find('o')}")
result = (f"Not found return -1 value if not found in list  {a.find('t')}") #return -1 value
print(result)
b = list(a)
print(f"split: {a.split('o')}")
print(b)
for i in range(len(b)):
    print(i)
    if b[i] == "o":
        print( f"found o at {i}")
print(f"found index of {a.index('o')}")
#print(f"found index of {a.index('t')}")  showing error

c = "pooja!!!"
print(f"rtrip: {c.rstrip('!')}")
print(len(c))
print(f"centre: {c.center(25)}")
print(f"len of centre: {len(c.center(25))}")
print(f"count: {c.count('o')}")
print(f"endswith: {c.endswith('!')}")
print(f"endswith range: {c.endswith('o', 1, 3)}")
D = "WelcomeToTheConsole"
print(f"isalnum: {D.isalnum()}")
D = "Pooja0"
print(f"isalpha: {D.isalpha()}")

str1 = "Python is interpreted language"
print(f"starts with {str1.startswith('Python')}")
print(f"swapcase lower to upper and viceversa:  {str1.swapcase()}")



