# To check if a number is prime, we need a function. Let's call it isPrime.
# This function should take a number as input and return True if it's a prime number, and False if it's not.

#Prime number definiton
# Any number less than or equal to 1 is not prime.
# A prime number is only diviside by itself and 1

#create your isPrime function. Make sure to include an appropriate function header. Remember, your function should return either True or False (no double quotes around it, just type True or False as is)
def isPrime(num):
    if num <= 1:
        return False

    for val in range(num):
        if num%val == 0:
            return False

    return True


#outside of the function, prompt the user to enter a number


#call the function in the condition of an if statement. If the function returns True, then the if statement should run. The if statements states that the number is prime


#else, print that the number is not prime
