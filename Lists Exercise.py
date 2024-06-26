import random

# Input Tests
catNames = []  # declaring list
print("Testing taking in data with lists")
while True:
    print(
        "Enter the name of the cat "
        + str(len(catNames) + 1)
        + " (Or enter nothing to stop.): "
    )
    name = input()
    if name == "":
        break
    catNames = catNames + [name]  # adding to list
if len(catNames) != 0:
    print("The cat names are:")
    for name in catNames:
        print(" " + name)
else:
    print("ERROR: List is empty")
# Loops Test
print("Testing loops with lists")
for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

# Pets Test
myPets = ["Max", "Zero", "Titan"]
print("Enter a pet name: ")
name = input()
if name not in myPets:
    print("I do not have a pet named " + name)
else:
    print(name + " is my pet.")

# Magic 8 ball with Lists
messages = [
    "It is certain",
    "It is decidedly so",
    "Yes definitely",
    "Reply hazy try again",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful",
]
print(messages[random.randint(0, len(messages) - 1)])
