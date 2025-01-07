total_points = 0

def update_points(points):
    global total_points
    total_points += points

def display_points():
    return f"Total Points: {total_points}"

choice = ""
i = 0

while choice != "n":
    i += 1
    choice = input("Do you want to input another game (y or n): ")
    while choice.lower() != "y" and choice.lower() != "n":
        print("Invalid")
        choice = input("Do you want to input another game (y or n): ")

    if choice.lower() == "y":
        p = int(input(f"Points for gGame {i}: "))
        update_points(p)
    else:
        break

print(display_points())
