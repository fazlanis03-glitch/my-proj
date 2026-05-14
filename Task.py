#Task list project using json

import json

try:
    with open ("task.json", "r") as file:  #we are using r because we want to read not write (w)
        my_tasks = json.load(file)
except FileNotFoundError:
    my_tasks = []


while True:
    user_option = input("What would you like to do (add/view/complete/delete/quit): ").lower().strip()
    
    
    if user_option == "add":
        task_name = input("what would you like to add to the list: ")

        add = {"task": task_name, "completed" : False}
        my_tasks.append(add)
        with open("task.json", "w") as file:
            json.dump(my_tasks, file, indent = 4)
        
        #view section 
    elif user_option == "view":
        print("View section")
        if my_tasks == []:
            print("No task yet")
        else:
            count = 1
            for tasks in my_tasks:
                print(f"{count},{tasks['task']} - {tasks['completed']}")
                count += 1

        #complete section 
    elif user_option == "complete":
        count = 1 # we want to show the number of the task here 
        for tasks in my_tasks:
            print(f"{count},{tasks['task']} - {tasks['completed']}")
            count += 1
        try:
            task_number = int(input("Which task number do you want to mark as complete? "))
            my_tasks[task_number - 1]["completed"] = True #this changes the complete status
            with open("task.json", "w") as file:
                json.dump(my_tasks, file, indent=4) #.dump is used for saving data 
        except ValueError:
            print("Invalid Input")
        except IndexError:
            print("That task number does not exsist! ")


            #delete section - next step we are working on

    elif user_option == "delete":
        count = 1
        for tasks in my_tasks:
            print(f"{count},{tasks['task']} - {tasks['completed']}")
            count += 1

        try:
            task_number = int(input("which task number do you want to delete? "))
            my_tasks.pop(task_number - 1)  # .pop deletes the task that we type in according to the num
            with open("task.json", "w") as file:
                json.dump(my_tasks, file, indent=4)
        except ValueError:
            print("Invalud input")
        except IndexError:
            print("That task number doesn't exist!")
        
    elif user_option == "quit":
        break


