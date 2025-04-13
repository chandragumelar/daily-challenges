while True:
    try:
        age = int(input("Please enter your age in number format: ").strip())
        if 0 <= age <= 120:
            print(f"Your age is {age} years old.")
            break
        print("Unrealistic age. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

