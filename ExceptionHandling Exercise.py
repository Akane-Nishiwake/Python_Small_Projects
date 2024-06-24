# Write your code here :-)
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

#or
def spam2(divide):
    return 42 / divide
try:
    print(spam2(2))
    print(spam2(12))
    print(spam2(0))
    print(spame2(1))
except ZeroDivisionError:
    print('Error: Invalid Argument')
