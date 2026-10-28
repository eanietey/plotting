with open("ints.txt", "r") as file:
    for line in file:
        print("ages: ",  int(line)+10)
