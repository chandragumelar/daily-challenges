correct_pin = '2468'
attempts_left = 3

while attempts_left > 0:
    pin = input("Enter your PIN (or type 'forgot'): ").strip().lower()
    
    if pin == correct_pin:
        print("Access granted.")
        break
    elif pin == 'forgot':
        print("Please contact customer service.")
        break

    attempts_left -= 1

    if attempts_left:
        print(f"Incorrect PIN. {attempts_left} tries left.")
    else:
        print("Account locked.")

