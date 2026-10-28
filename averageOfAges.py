try:
    fhand = open("age.txt")
except:
    print("File cannot open")
    exit()



count = 0
total = 0

for line in fhand:
    diff = line.find(":")
    age = float(line[diff+1:])
    total += age
    count+=1
print(total/count)
