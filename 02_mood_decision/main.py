mood = input("How are you feeling? (happy/sad/etc): ").strip().lower()

if mood == 'happy':
    print("Keep smiling!")
else:
    time = input("What time is it? (day/night): ").strip().lower()
    
    if time == 'night':
        weather = input("What's the weather like? (rainy/clear/etc): ").strip().lower()
        
        if weather == 'rainy':
            print("Sleep tight.")
        else:
            print("Enjoy your night.")
    
    else:
        has_work = input("Do you have work? (yes/no): ").strip().lower()
        
        if has_work == 'yes':
            print("Get to work!")
        else:
            print("Relax and chill.")

