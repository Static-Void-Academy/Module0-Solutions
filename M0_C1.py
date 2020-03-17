# Script will start by asking for name, greeting user, and then
# listing off locations. Output and next steps depend on user's
# input. See https://github.com/Static-Void-Academy/Module0-Challenges/blob/master/M0.C1.md

print('Hello! What is your name?')
name = input()

print(f'Welcome to SVA, {name}! Where would you like to go?')
print('Choose from: Cafeteria, Office, Playground, Restroom')
location = input()

if location == 'Cafeteria':
    print('The Cafeteria is straight ahead at the end. Enjoy!')
elif location == 'Office':
    print('The Office is up the stairs and to the left.')
elif location == 'Playground':
    print('Please confirm your age:')
    age = int(input())
    if age <= 11:
        print('Our Playground is back out the main door and around the side.')
    else:
        print('Sorry, you are too old!')
elif location == 'Restroom':
    print('The Restroom is down the hall and to the right before the cafeteria.')

