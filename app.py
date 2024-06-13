from models.user import User
from models.workout import Workout
from models.goal import Goal
from models.membership import Membership
import time
from datetime import datetime

def create_workout(user_id):
    type = input("Enter workout type (e.g., Cardio, Strength): ")
    duration = int(input("Enter workout duration (in minutes): "))
    calories_burned = int(input("Enter calories burned: "))
    while True:
        date_str = input("Enter workout date (YYYY-MM-DD): ")
        try:
            workout_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    timestamp = int(workout_date.strftime('%s'))

    Workout.create(user_id=user_id, type=type, duration=duration, calories_burned=calories_burned, date=timestamp)
    print("Workout created successfully!")

def create_goal(user_id):
    description = input("Enter goal description: ")
    target_date = input("Enter target date (YYYY-MM-DD): ")
    
    Goal.create(user_id=user_id, description=description, target_date=target_date)
    print("Goal created successfully!")

def register_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    full_name = input("Enter full name: ")

    user_id = User.create(username=username, email=email, full_name=full_name)
    if user_id is not None:
        print(f"User created successfully! Your user ID is {user_id}")

        print("Choose a membership plan:")
        print("1. Bronze")
        print("2. Silver")
        print("3. Gold")
        plan_choice = input("Enter your choice: ")
        plan_mapping = {"1": "Bronze", "2": "Silver", "3": "Gold"}
        plan = plan_mapping.get(plan_choice)
        if plan is None:
            print("Invalid choice. Defaulting to Bronze plan.")
            plan = "Bronze"

        start_date = input("Enter membership start date (YYYY-MM-DD): ")
        end_date = input("Enter membership end date (YYYY-MM-DD): ")

        Membership.create(user_id=user_id, plan=plan, start_date=start_date, end_date=end_date)
        print("Membership created successfully!")

        while True:
            create_workout(user_id)
            add_another = input("Would you like to add another workout? (yes/no): ").strip().lower()
            if add_another != 'yes':
                break

        while True:
            create_goal(user_id)
            add_another = input("Would you like to add another goal? (yes/no): ").strip().lower()
            if add_another != 'yes':
                break
    else:
        print("Failed to create user.")

def view_existing_members():
    users = User.get_all()
    print("\nUsers:")
    for user in users:
        print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Full Name: {user[3]}")

def get_user_details(user_id):
    user = User.find_by_id(user_id)
    if user:
        print(f"User Details - ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Full Name: {user[3]}")
    else:
        print("User not found.")

def specific_member_progress():
    specified_user_id = input("Enter user ID to retrieve progress: ")

    print("\nUser Details:")
    get_user_details(specified_user_id)

    print("\nWorkouts:")
    workouts = Workout.find_by_user_id(specified_user_id)
    if workouts:
        for workout in workouts:
            print(f"ID: {workout[0]}, User ID: {workout[1]}, Type: {workout[2]}, Duration: {workout[3]}, Calories Burned: {workout[4]}, Date: {datetime.utcfromtimestamp(workout[5]).strftime('%Y-%m-%d')}")
    else:
        print("No workouts found for the specified user.")

    print("\nGoals:")
    goals = Goal.find_by_user_id(specified_user_id)
    if goals:
        for goal in goals:
            print(f"ID: {goal[0]}, User ID: {goal[1]}, Description: {goal[2]}, Target Date: {goal[3]}")
    else:
        print("No goals found for the specified user.")

    print("\nMemberships:")
    user_membership = Membership.find_by_user_id(specified_user_id)
    if user_membership:
        print(f"ID: {user_membership[0]}, User ID: {user_membership[1]}, Plan: {user_membership[2]}, Start Date: {user_membership[3]}, End Date: {user_membership[4]}")
    else:
        print("Membership not found for the specified user ID.")

def delete_user():
    user_id = input("Enter user ID to delete: ")
    User.delete_by_id(user_id)
    print("User deleted successfully!")

def update_user_details_menu(user_id):
    while True:
        print("\nUpdate User Details Menu:")
        print("1. Update user workout")
        print("2. Update user goals")
        print("3. Go back")

        choice = input("Enter your choice: ")

        if choice == '1':
            update_user_workout(user_id)
        elif choice == '2':
            update_user_goals(user_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

def update_user_workout(user_id):
    create_workout(user_id)

def update_user_goals(user_id):
    create_goal(user_id)

def main():
    while True:
        print("\nMenu:")
        print("1. Register a new user")
        print("2. View existing members")
        print("3. View specific member progress")
        print("4. Update user details")
        print("5. Delete a user")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            view_existing_members()
        elif choice == '3':
            specific_member_progress()
        elif choice == '4':
            user_id = input("Enter user ID to update details: ")
            update_user_details_menu(user_id)
        elif choice == '5':
            delete_user()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
