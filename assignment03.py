print("Welcome to the Counting Game!\n")

count = 0

def increase_count():
    global count
    count += 1

def reset_count():
    global count
    count = 0


while True:
    choice = input("Would you like (I)ncrease or (R)eset the count (STOP to exit)? ").upper()

    if (choice == "STOP"):
        break
    elif (choice == "INCREASE" or choice == "I"):
        increase_count()
    elif (choice == "RESET" or choice == "R"):
        reset_count()
    else:
        print("Invalid input.  Please try again.")

    print(f"The current count is {count}.")

print(f"The final count is {count}.")
print("Thanks for playing the game!")

