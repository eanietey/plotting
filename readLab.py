with open("pets.txt", "r") as file:
    for word in file:
        search = word.find("s")
        space = word[:search].rstrip()
        print(space)
