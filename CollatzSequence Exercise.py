# Write your code here :-)
import sys

def collatz(number):
    if number % 2 == 0:
        num = number // 2
        print(num)
        return num
    else:
        num = 3 * number + 1
        print(num)
        return num


print("Please enter a number: ")
while True:
    try:
        userInput = int(input())
        while userInput != 1:
            userInput = collatz(userInput)
        break
    except ValueError:
        print("Please enter a valid integer:")
