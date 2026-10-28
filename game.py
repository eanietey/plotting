from game_fxns import *
'''
true_num = get_number()
guess = float(input("Guess a number between 1 and 15: "))
check(guess, true_num)
print("Game over. True number was: ", true_num)
'''
i = 0
x = get_number()



choice = input("Choose a level: 1.Easy 2.Hard.... " )

if choice == "hard" or choice == "Hard":
    
    while i < 3:
        guess = int(input("Guess a number between 1 anad 15: "))
        result = check(guess, x)

        if guess == x:
            break
    
        i = i+1
    
    print("Game over. True number was: ", x)

elif choice == "easy" or choice == "Easy":
    
    while i < 6:
        guess = int(input("Guess a number between 1 anad 15: "))
        result = check(guess, x)

        if guess == x:
            break
    
        i = i+1
    
    print("Game over. True number was: ", x)
