#password manager code



#master password option  
master_password = 122349
   
attempts = 3 #limit of attempts they start with
while attempts > 0:
        try: 
            master_option = int(input("Please enter Master Password: "))
        except ValueError:
            print("invalid input, numbers only")
            attempts -= 1
            continue
        if master_option == master_password:
            break
        else:
            attempts -= 1 #this will show the user how many attemps left after guessing
            print(f"Incorrect! you have {attempts} attempts left")
            
        if attempts == 0:
            print("Too many failed attempts, Exiting program")
            exit()

while True:
    user_option = input("What would you like to do (add/view/quit): ").lower().strip()



    if user_option == 'view': 
        try:
            with open("passwords.txt", "r") as f: # this saves it in our passwords.txt file - where all the passwords are saved 
                for line in f:
                    print(line.strip()) 
        except FileNotFoundError:
            print("No saved password, Add one first")
    elif user_option == 'add':
        account = input("Account/Website name: ").strip()
        username = input("Username: ").strip() 
        password = input("Password: ").strip()
        with open('passwords.txt', "a") as f:
            f.write(f"{account} | {username} | {password}\n") 
    elif user_option == 'quit':
        break
    else:
        print("Invalid selection")


