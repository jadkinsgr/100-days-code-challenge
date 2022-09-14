from Art import logo
import random
print(logo)

version = input("How would you like to play? Please type 'Easy' or 'Hard'")

if version == 'Hard':
    tryCount = 5
if version == 'hard':
    tryCount = 5
else:
    tryCount = 10

number = random.randrange(0,100)

print(f"You have selected the {version} version. You now have exactly {tryCount} trys to guess the correct number between 0 and 100. Good luck!")