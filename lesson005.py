hello = ""
def hi():
    global hello
    hello = "Hello"

hi()
print(hello)