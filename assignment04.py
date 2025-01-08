def calculate_sum(start, stop):
    if start == stop:
        return stop
    else:
        return start + calculate_sum(start+1, stop)

def calculate_product(start, stop):
    if start == stop:
        return stop
    else:
        return start * calculate_product(start+1, stop)


while True:
    try:
        start = int(input("Please enter the start value: "))
        stop = int(input("Please enter the stop value: "))
        print(f"The sum of the values between {start} and {stop} is {calculate_sum(start, stop)}.")
        print(f"The product of the values between {start} and {stop} is {calculate_product(start, stop)}.")

        choice = input("Do you want to continue? (YES/NO): ")
        if choice.lower() == "no":
            break

    except ValueError:
        print("Please enter valid integers.")

