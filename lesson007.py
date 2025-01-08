def sum(start, stop):
    if start == stop:
        return stop
    else:
        return start + sum(start+1, stop)

def product(start, stop):
    if start == stop:
        return stop
    else:
        return start * product(start+1, stop)


while True:
    try:
        start = int(input("Please enter the start value: "))
        stop = int(input("Please enter the stop value: "))
        print(f"The sum of the values between {start} and {stop} is {sum(start, stop)}.")
        print(f"The product of the values between {start} and {stop} is {product(start, stop)}.")

        choice = input("Do you want to continue? (YES/NO): ")
        if choice.lower() == "no":
            break

    except ValueError:
        print("Please enter valid integers.")
