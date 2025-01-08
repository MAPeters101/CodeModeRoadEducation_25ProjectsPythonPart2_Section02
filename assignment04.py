# Give a header title for the recursive function that calculates the sum of all numbers in the range.


# Base case: Check if start and stop are the same, return the value.

# Replace this line with the return statement for the base case

# Recursive case: Add the current start to the sum of the rest.

# Replace this line with the return statement for the recursive case


# Give a header title for the recursive function that calculates the product of all numbers in the range.


# Base case: Check if start and stop are the same, return the value.

# Replace this line with the return statement for the base case

# Recursive case: Multiply the current start with the product of the rest.

# Replace this line with the return statement for the recursive case


# Main program
while True:
    try:
        # User input for start and stop numbers (stored into two variables)

        # Calculate (call the sum function) and print that value

        # Calculate (call the product function) and print the product

        # Ask if the user wants to continue
        choice = input("Do you want to continue? (YES/NO): ")

        # if choice is "NO" - check lowercase, then break out of the loop


    except ValueError:
        print("Please enter valid integers.")

