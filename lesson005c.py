x = 5
def inc():
    global x
    x = 10
    return x

print(f"Outside the function: {x}")
print(f"Inside the function: {inc()}")
print(f"Outside the function: {x}")
