attempts = 0

while True:
    attempts += 1
    raw = input("Enter numbers separated by commas: ").strip()
    
    try:
        numbers = [int(n.strip()) for n in raw.split(",")]
        break
    except ValueError:
        print("Invalid input. Try again.")

evens = [n for n in numbers if n % 2 == 0]

print(f"Even numbers: {evens}")
print(f"Count: {len(evens)}")
print(f"Took {attempts} {'try' if attempts == 1 else 'tries'} to enter valid input.")

attempts = 0

while True:
    attempts += 1 
    raw = input('enter numbers separated by commas: ').strip()

    try:
        numbers = [int(n.strip()) for n in raw.split(",")]
        break
    except ValueError:
        print('please input valid number')

evens = [n for n in numbers if n % 2 == 0]
