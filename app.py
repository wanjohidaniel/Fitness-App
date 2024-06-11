# app.py

from database.setup import create_tables
from models.user import User
from models.workout import Workout
from models.goal import Goal

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    username = input("Enter username: ")
    email = input("Enter email: ")
    full_name = input("Enter full name: ")

    # Create a user and retrieve its ID
    user_id = User.create(username=username, email=email, full_name=full_name)

    # Retrieve and print the created user
    user = User.find_by_username(username)
    if user:
        print(f"User created successfully with ID: {user_id}")
        print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Full Name: {user[3]}")
    else:
        print("Failed to retrieve user information.")

    # Collect workout input
    date = input("Enter workout date: ")
    workout_type = input("Enter workout type: ")
    duration = int(input("Enter workout duration (in minutes): "))
    calories_burned = int(input("Enter calories burned: "))

    # Create a workout
    workout_id = Workout.create(user_id=user_id, date=date, type=workout_type, duration=duration, calories_burned=calories_burned)

    # Retrieve and print the created workout
    workout = Workout.find_by_id(workout_id)
    if workout:
        print(f"Workout created successfully with ID: {workout_id}")
        print(f"ID: {workout[0]}, User ID: {workout[1]}, Date: {workout[2]}, Type: {workout[3]}, Duration: {workout[4]}, Calories Burned: {workout[5]}")
    else:
        print("Failed to retrieve workout information.")

    # Collect goal input
    description = input("Enter goal description: ")
    target_date = input("Enter target date for the goal: ")

    # Create a goal
    goal_id = Goal.create(user_id=user_id, description=description, target_date=target_date)

    # Retrieve and print the created goal
    goal = Goal.find_by_id(goal_id)
    if goal:
        print(f"Goal created successfully with ID: {goal_id}")
        print(f"ID: {goal[0]}, User ID: {goal[1]}, Description: {goal[2]}, Target Date: {goal[3]}")
    else:
        print("Failed to retrieve goal information.")

if __name__ == "__main__":
    main()
