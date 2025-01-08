# Give a header title for the recursive function that calculates the sum of all numbers in the range.
def calculate_sum(start, stop):

    # Base case: Check if start and stop are the same, return the value.
    if start == stop:
        return stop
    # Replace this line with the return statement for the base case

    # Recursive case: Add the current start to the sum of the rest.
    else:
    # Replace this line with the return statement for the recursive case
        return stop + calculate_sum(start, stop-1)

# Give a header title for the recursive function that calculates the product of all numbers in the range.


# Base case: Check if start and stop are the same, return the value.

# Replace this line with the return statement for the base case

# Recursive case: Multiply the current start with the product of the rest.

# Replace this line with the return statement for the recursive case


# Main program
while True:
    try:
        # User input for start and stop numbers (stored into two variables)
        start = int(input("Please enter the start value: "))
        stop = int(input("Please enter the stop value: "))
        # Calculate (call the sum function) and print that value
        print(f"The sum of the values between {start} and {stop} is {calculate_sum(start, stop)}.")

        # Calculate (call the product function) and print the product

        # Ask if the user wants to continue
        choice = input("Do you want to continue? (YES/NO): ")

        # if choice is "NO" - check lowercase, then break out of the loop
        if choice.lower() == "no":
            break

    except ValueError:
        print("Please enter valid integers.")

