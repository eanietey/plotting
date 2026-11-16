def linear(m,x,b):
    return m*x+b

def slope_units(x_units, y_units):
    
    unit = x_units.rstrip("s")
    unit1 = y_units.rstrip("s")

    return unit1 + "/" + unit

def print_equation(m, b, x_units, y_units):
    s = slope_units(x_units, y_units)
    print ("The equation of the line is: y =", m ,s, "+",  b, y_units)

