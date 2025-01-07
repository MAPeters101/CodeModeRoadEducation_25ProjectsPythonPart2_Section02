import random

def getInteger():
    return random.randint(1, 100)

choice = ""
while choice != "no":
    choice = input("Would you like a random number? (Input no to exit) ")
    choice = choice.lower()
    if choice == 'no':
        break
    else:
        print(getInteger())