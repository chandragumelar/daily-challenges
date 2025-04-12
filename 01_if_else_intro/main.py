name = input('what is your name? ')

if name == 'Bob':
    print('Hey Bob')
else:
    age = int(input('how old are you? '))
    if age < 18:
        print('too young')
    elif input('which country are you from? ').strip().lower() == 'usa':
        print('welcome american')
    else:
        print('access denied')

