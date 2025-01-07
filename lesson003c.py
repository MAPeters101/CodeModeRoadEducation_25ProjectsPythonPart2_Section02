import random

def getInteger():
    return random.randint(1, 101)

while True:
    choice = input("Would you like a number? ")
    if choice.lower() == 'no':
        break
    print(getInteger())