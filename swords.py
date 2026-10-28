

try:
    fhand = open('MarriageAges-1.csv')
      

except:
    print("File cannot open")
    exit()

            
next(fhand)
l = []
for line in fhand:
    nums = line.split(",")
    h_age = nums[0]
    w_age = nums[1].strip()
    l.append(h_age)
    l.append(w_age)
print(l)
