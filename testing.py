name = input("Enter your name: ")

space = name.find(" ")
first = name[:space]
second = name[space:]

print(first)
print(second)

i=0
while i < 4:
    value = input("Enter any mammal name: ")

    pointdiff = value.find("a")

    if pointdiff:
        frac = value[:pointdiff]
        print(frac)
    else:
        print(value)
    i+=1
print("Out of tries")
