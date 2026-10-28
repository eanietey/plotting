import random
''' 
Generate a random number: Use randint() from the random module (library)
to generate a random number betw
'''

'''Check the guess: Compare the user's guess to the random number (called true_number).
If the guess is correct, return True 
and print a congratulatory message.
If the guess is too high, return False and
print a message telling the user to guess lower.
If the guess is too low, return False and
print a message telling the user to guess higher. '''

def get_number():
    num = random.randint(1, 15)
    return num


'''
i = 0
x = get_number()

while i < 6:
    guess = int(input("Guess a number between 1 anad 15: "))
    result = check(guess, x)

    if guess == x:
        break

    print(result)
    i = i+1
    
print("done")
'''

def check(guess, tr):

    if guess == tr:
        print("Congratulations")
        return True
    elif guess > tr:
        print("Guess lower")
        return False
    elif guess < tr:
        print("Guess higher")
        return False
   

