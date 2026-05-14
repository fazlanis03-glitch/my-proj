#random dice roll

import random

#loop 
while True:

    choice = input('Roll the dice? (y/n): ').lower()

    class Dice:
        def roll(self):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            return die1, die2
    dice = Dice()


    if choice == 'y':
        die1, die2 = dice.roll() 
        print(f'({die1}, {die2})')

    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid input. Please enter "y" or "n".')   

     


