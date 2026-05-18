#workout logger
import json
from datetime import date


try:
    with open ("workout.json", "r") as file:  #we are using r because we want to read not write (w)
        my_workout = json.load(file)
except FileNotFoundError:
    my_workout = []

while True:
    user_option = input("Which option would you like to select (Log/view/progress/pr/quit)? ").lower().strip()

    if user_option == "log":
        exercise = input("Enter the name of the exercise: ")
        sets = int(input("Enter the number of sets: "))
        reps = int(input("Enter the number of reps: "))
        weight = int(input("Enter the weight used: "))
        workout_date = date.today().strftime("%Y-%m-%d")

        #dictionary
        workout_entry = {
            "exercise": exercise,
            "sets": sets,
            "reps": reps,
            "weight": weight,
            "date": workout_date
        }
        my_workout.append(workout_entry) #this adds the workout entry to the list of workouts
        with open("workout.json", "w") as file: #save to file
            json.dump(my_workout, file, indent=4)

    elif user_option == "view":
        if my_workout == []:
            print("No workout have been logged yet.")
        else:
            count = 1
            for workout in my_workout:
                print(f"{count}. {workout['exercise']} - {workout['sets']} sets - {workout['reps']} reps - {workout['weight']} lbs - {workout['date']}")
                count += 1


    elif user_option == "progress":
        exercise_name = input("Enter the name of the exercise: ")
        exercise_progress = [workout for workout in my_workout if workout["exercise"].lower() == exercise_name.lower()]
        if exercise_progress == []:
            print(f"No progress found for {exercise_name}.")
        else:
            print(f"Progress for {exercise_name}:")
            for workout in exercise_progress:
                print(f"{workout['date']}: {workout['sets']} sets - {workout['reps']} reps - {workout['weight']} lbs")



    elif user_option == "pr":
        exercise_name = input("Enter the name of the exercise: ")
        pr = max([workout["weight"] for workout in my_workout if workout["exercise"].lower() == exercise_name.lower()], default=0)
        if pr == 0:
            print(f"No PR found for {exercise_name}.")
        else:
            print(f"Your PR for {exercise_name} is {pr} lbs.")


    elif user_option == "quit":
        break 