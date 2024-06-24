# Write your code here :-)
import time, sys
indent = 0 #spaces to indent
isIndentIncrease = True #does the indent increase or not
try:
    while True:
        print(' ' * indent, end='')
        print('*******')
        time.sleep(0.1)

        if isIndentIncrease:
            indent = indent + 1
            if indent == 20:
                isIndentIncrease = False

        else:
            indent = indent - 1
            if indent = 0:

