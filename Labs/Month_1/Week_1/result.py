username = input('Enter your username: ')
score = input('Enter your jamb score: ')
if score == 150:
    print('You tried, but you can do better ' + username)
elif score == 250:
    print('Good job ' + username)
elif score == 350:
    print('Excellent job ' + username)
else:
    print('You did not study hard ' + username)

print('You can always check back later ')
