# daily_reminder.py

# 1. Prompt for a single task
task = input("Enter your task: ")

# 2. Prompt for the task's priority and normalize to lowercase
priority = input("Priority (high/medium/low): ").strip().lower()

# 3. Prompt whether the task is time-bound (yes/no)
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# 4. Determine base message based on priority using match-case
match priority:
    case "high":
        base_msg = f"'{task}' is a high priority task"
    case "medium":
        base_msg = f"'{task}' is a medium priority task"
    case "low":
        base_msg = f"'{task}' is a low priority task"
    case _:
        # If the user typed something other than high/medium/low
        base_msg = f"'{task}' has an unknown priority"

# 5. Adjust the reminder depending on time sensitivity
if time_bound == "yes":
    # Time-bound means “immediate attention”
    print(f"Reminder: {base_msg} that requires immediate attention today!")
else:
    # Not time-bound: more relaxed wording
    print(f"Note: {base_msg}. Consider completing it when you have free time.")

# 6. Final congratulatory message with a “tweet” prompt
print()
print("Well done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")
