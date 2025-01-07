def isPrime(num):
  if num <= 1:
    return False

  for i in range(2, num):
    if num % i == 0:
      return False

  return True

number = int(input("Enter a number: "))

if isPrime(number):
  print(f"{number} is prime")

else:
  print(f"{number} is not prime")