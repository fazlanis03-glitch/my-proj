#rock, paper, scissors game

#refactored code - this make the code easier whenever u have long lines of code and need to call things again 

import random

#declaring constats under - we changed the emojis section the originally had R,P,S now we have the actual spelling
#we did this to make the code more cleaner as well as more readable
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

Emojis = {
    ROCK : 'Rock 🪨', 
    PAPER : 'Paper 📄',
    SCISSORS : 'Scissors ✂️'

    }
options = (tuple(Emojis.keys())) #this has (r, p, s) init the tuple command was able to store 


while True:
    def get_user_option():
        users_option = input('Do you want to choose rock, paper, or scissors (r, p, s): ').lower()
        if users_option in options:
            return users_option
        else:
            print('Invalid Choice')
        


        #bec we moved everything we must pass the names of our functions in the () of the def types
    def display_choices(users_option, computer_choice):

        print('you chose:', Emojis.get(users_option, users_option)) #this shows the users pick

        print('Computer chose:',Emojis.get(computer_choice, computer_choice)) #this shows the computers pick

#when moving below section to here we get an error bec of indentation but that can be resolved by indenting 
    def determine_winner(users_option, computer_choice):
            if users_option == computer_choice:
                print("It's a Tie")
            elif (
                (users_option == ROCK and computer_choice == SCISSORS) or
                (users_option == SCISSORS and computer_choice == PAPER) or
                (users_option == PAPER and computer_choice == ROCK)):
                print("You Win")
            else:
                print("You Lost")


    def play_game():
        while True:

        #bec we moved user_option above we have to call it again
            users_option = get_user_option() #this calls the get_user_option method that we made above
  
    
        

            computer_choice = random.choice(options) 

        
            display_choices(users_option, computer_choice) #this calls display_choices 


            determine_winner(users_option, computer_choice)

#play again step

            Again = input("Continue (y/n): ").lower()
            if Again == 'y':
                continue 
            elif Again == 'n':
                break
            else:
                print("Invalid input, select (y,n)")

                
    play_game() #we have to call this at the end now because the program is different and this is what lets us start it
    #watch where the indentation is as well for this line because it is suppose to be outside the loops 