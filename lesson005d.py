total_points = 0

def update_points(points):
    global total_points
    total_points += points

def display_points():
    return f"Total Points: {total_points}"

update_points(5)
update_points(20)
update_points(15)

print(display_points())