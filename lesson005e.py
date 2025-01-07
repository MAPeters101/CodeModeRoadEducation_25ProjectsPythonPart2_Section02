total_points = 0

def update_points(points):
    global total_points
    total_points += points

def display_points():
    return total_points

game = 1

while game <= 3:
    while True:
        points = int(input(f"Enter the points for game{game} (-1 to quit): "))
        if points == -1:
            print(f"The total number of points for Game{game} is {display_points()}")
            #print(display_points())
            break
        update_points(points)
    game += 1
    total_points = 0

