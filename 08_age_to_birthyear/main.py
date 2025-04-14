from datetime import datetime

current_year = datetime.now().year

while True:
    try:
        age = int(input("Please enter your age: ").strip())
        if 0 <= age <= 120:
            birth_year = current_year - age
            print(f"You were born in {birth_year}.")
            break
        print("Unrealistic age. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

