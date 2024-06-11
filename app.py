from database.setup import create_tables
from models.user import User
from models.workout import Workout
from models.goal import Goal
from models.membership import Membership

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    username = input("Enter username: ")
    email = input("Enter email: ")
    full_name = input("Enter full name: ")

    # Create a user and retrieve its ID
    user_id = User.create(username=username, email=email, full_name=full_name)
    if user_id is not None:
        print("User created successfully!")
    else:
        print("Failed to create user.")

    # Retrieve and print all users
    users = User.get_all()
    print("\nUsers:")
    for user in users:
        print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Full Name: {user[3]}")

    # Collect workout input
    date = input("Enter workout date: ")
    workout_type = input("Enter workout type: ")
    duration_input = input("Enter workout duration in minutes: ")
    duration = int(''.join(filter(str.isdigit, duration_input)))  # Extract numeric characters
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

    # Collect membership input
    plan = input("Enter membership plan: ")
    start_date = input("Enter membership start date: ")
    end_date = input("Enter membership end date: ")

    # Create a membership
    Membership.create(user_id=user_id, plan=plan, start_date=start_date, end_date=end_date)

    # Retrieve and print all memberships
    memberships = Membership.get_all()
    print("\nMemberships:")
    for membership in memberships:
        print(f"ID: {membership[0]}, User ID: {membership[1]}, Plan: {membership[2]}, Start Date: {membership[3]}, End Date: {membership[4]}")

    # Retrieve membership information for a specified user ID
    specified_user_id = input("Enter user ID to retrieve membership information: ")
    user_membership = Membership.find_by_user_id(specified_user_id)
    if user_membership:
        print("\nMembership Information:")
        print(f"ID: {user_membership[0]}, User ID: {user_membership[1]}, Plan: {user_membership[2]}, Start Date: {user_membership[3]}, End Date: {user_membership[4]}")
    else:
        print("Membership not found for the specified user ID.")

if __name__ == "__main__":
    main()
