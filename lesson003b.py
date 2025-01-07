def helloWorld():
    return "Hello World"

def iLikePython():
    return "I like Python"

def imBored():
  return "I'm bored"

choice = ""

while choice != "STOP":
    choice = input("What message do you want (1, 2, 3, STOP)? ")
    if choice.upper() == "STOP":
        break
    while not(1 <= int(choice) <= 3):
        choice = input("What message do you want (1, 2, 3)? ")

    if int(choice) == 1:
        print(helloWorld())
    elif int(choice) == 2:
        print(iLikePython())
    elif int(choice) == 3:
        print(imBored())


