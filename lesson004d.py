def greeting(em, ch, un="Guest"):
    if ch == True:
        return f"Hello {un}"
    return f"Hello {em}"


email = input("Enter your email: ")
choice = input("Do you want to enter your username: ")

if choice.lower() == "yes" or choice.lower() == "y":
    username = input("Enter your username: ")
    x = greeting(email, True, username)
else:
    x = greeting(email, False)

print(x)

