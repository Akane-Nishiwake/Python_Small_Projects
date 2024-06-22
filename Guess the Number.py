# Write your code here :-)
import random  # importing the related module

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
for guessessTaken in range(1, 7):  # users get 7 guesses
    print("Take a guess.")
    guess = int(input())
    if guess < secretNumber:
        print("Your number is too low")
    elif guess > secretNumber:
        print("Your number is too high")
    else:
        break  # this is the correct number condition
if guess == secretNumber:
    print("Good job you got the number in " + str(guessessTaken) + " guesses!")
else:
    print("Sorry the number was " + str(secretNumber))
