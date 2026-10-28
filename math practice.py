import math as m

calc = 1/(2*(m.pi))

print(calc)

if calc < 1:
    print("This i s plausible")
else:
    print("This is incorrect")

try:
    degIn = float(input("Enter your angle in degrees: "))
    radCalc = degIn * (m.pi/180)
    print("Your angle is ", radCalc, " in radians")

    if degIn < 0:
        print("No numbers
              below  0")
    elif degIn > 0 and degIn < 90:
        print("Angle in Quadrant 1")
    elif degIn > 90 and degIn < 180:
        print("Angle in Quadrant 2")
    elif degIn > 180 and degIn < 270:
        print("Angle in Quadrant 3")
    elif degIn > 270 and degIn < 360:
        print("Angle in Quadrant 4")
except:
    print("Invalid input")



