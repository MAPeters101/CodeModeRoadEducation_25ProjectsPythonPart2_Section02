print("Welcome to the Counting Game!\n")

#initialize the count variable, setting it equal to 0
count = 0

# create a function to increase the count. Make sure to use the global keyword followed by the count variable name
def increase_count():
    global count
    count += 1


# create a function to reset the count. Make sure to use the global keyword followed by the count variable name
def reset_count():
    global count
    count = 0

# Main game loop
while True:

  #first ask the user if they want to increase the count, reset the count, or stop the count
    choice = input("Would you like (I)ncrease or (R)eset the count (STOP to exit)? ").upper()

  #then use conditionals to call the appropriate function based on user's input
    if (choice == "STOP"):
        break

      # End the game if the player types 'stop' (HINT: just break)
    elif (choice == "INCREASE" or choice == "I"):
        increase_count()
    elif (choice == "RESET" or choice == "R"):
        reset_count()
    else:
        print("Invalid input.  Please try again.")

  #if the user didn't enter 'increase', 'reset', or 'stop', print that their input was not valid (HINT: simply just use an else statement)


  #at the end of each loop, print the current count value
    print(f"The current count is {count}.")


#outside of the loop, print the final count value
print(f"The final count is {count}.")


print("Thanks for playing the game!")

