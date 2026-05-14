
import random

secret_number = random.randint(1,100)

counter = 0 #so this starts at zero before we start loop 

while True:
    User_selection = input("Select a number from 1-100: ")
    try:
        guesses = int(User_selection)
        counter += 1 #guess counter 
    except ValueError:
        print("Invalid input")
        continue



    if guesses == secret_number:
        print("You guessed correct !")
        print(f'you got it in {counter} guesses')

        break
    elif guesses > secret_number:
        print("Your number is too high")
    else:
        print("your number is too low")