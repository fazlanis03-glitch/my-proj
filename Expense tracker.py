#Expense tracker
#program where income, expenses, and we can do more


import json

try:
    with open ("Expense.json", "r") as file:  #we are using r because we want to read not write (w)
        my_tracker = json.load(file)
except FileNotFoundError:
    my_tracker = []

while True: #while true and try need to be within the same indent 
        user_option = input("Which option would you like to select (add income/add expense/view/balance/quit)? ").lower().strip()


        if user_option == "add income":
            amount = int(input("Enter amount: "))
            category = input("Enter category (salary/gift/bonus): ")
            description = input("Enter description: ")
           
        #dictionary 
        transaction = {
            "type" : "income", 
            "amount" : amount, 
            "category" : category, 
            "description" : description
        }

        my_tracker.append(transaction) #add transaction to the list
        with open("Expense.json","w" ) as file:
            json.dump(my_tracker, file, indent = 4) #saving to json file

        #whats next run program make sure its working then move on
        
        elif user_option == "add expense":
            print("add expense")


        elif user_option == "view":
            print("view")



        elif user_option == "balance":
            print("balance")


        elif user_option == "quit":
            break