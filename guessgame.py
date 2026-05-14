#program excercise number 2


#- Generate a random number between 1 and 100
#- User types in a guess
#- If the guess is too high, print: "too high"
#- If the guess is too low, print: "too low"
#- Keep letting the user try again
#- If the user guesses correctly, print: "you have guessed the number"



import random

# we don't need a class here
random_number = random.randint(1, 100)  # one secret number for the whole game

while True:
    user_input = input("Enter a random number (1-100): ")

    try:
        result = int(user_input)  # convert the user's input, not the secret number
    except ValueError:
        print("Not valid")
        continue

    if result == random_number:
        print("You guessed correct!")
        break
    elif result < random_number:
        print("guess is too low")
    else:
        print("guess is too high")
     


 