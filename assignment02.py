def isPrime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True

    for val in range(2, num):
        if num%val == 0:
            return False

    return True


number = int(input("Please enter a number to check to see if it is a prime number: "))

if isPrime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
