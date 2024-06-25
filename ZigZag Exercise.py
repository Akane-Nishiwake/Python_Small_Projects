# Write your code here :-)
import time, sys

indent = 0  # spaces to indent
isIndentIncrease = True  # does the indent increase or not
try:
    while True:
        print(" " * indent, end="")
        print("*******")
        time.sleep(0.1)#allows for the program to run smoothly

        if isIndentIncrease:
            indent = indent + 1
            if indent == 20:
                isIndentIncrease = False#Change direction

        else:
            indent = indent - 1
            if indent == 0:
                isIndentIncrease = True#Change direction
except KeyboardInterrupt:#Ctrl + C to interrupt program
    sys.exit()#exit program
