def factorial(n):
    if n==0:
        return 1
    else:
        x = n * factorial(n-1)
        return x

num = 5

for i in range(num):
    print(f"The factorial of {i} is {factorial(i)}.")
