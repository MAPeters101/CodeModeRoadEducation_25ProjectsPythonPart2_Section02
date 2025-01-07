#this is where you should add your orderSummary function
def orderSummary():
  print("-------------------------------\n")
  print("Order Summary:")
  print(f"Pizza Size: {size_out}")
  print(f"Topping: {topping_out}")
  print(f"Drink: {drink_out}")
  print("Total Cost: ${:.2f}".format(price))

price = 0
print("Welcome to Pizza Paradise!")
size_out = "None"
topping_out = "None"
drink_out = "None"

print("\nAvailable Pizza Sizes:")
print("1. Small ($10) \n2. Medium ($15) \n3. Large ($20)")
size = int(input("\nChoose your pizza size (1/2/3): "))
if size > 3 or size < 1:
  print("\nInvalid Choice\nRe-run the program to get new pizza.")
  size_out = "None"
else:
  if size == 1:
    price += 10
    size_out = "Small"
  elif size == 2:
    price += 15
    size_out = "Medium"
  elif size == 3:
    price += 20
    size_out = "Large"

#ask the user if they want to see the order summary here
choice = input("Would you like to see your order summary (y or yes)? ").lower()
if choice == 'y' or choice == 'yes':
  orderSummary()

print("\nAvailable Pizza Toppings:")
print("1. Pepperoni ($2) \n2. Mushrooms ($1.50) \n3. Onions ($1) \n4. Extra Cheese ($1.75)")
topping = int(input("\nChoose one topping (1/2/3/4): "))
if topping > 4 or topping < 1:
  print("\nInvalid Choice\nRe-run the program for toppings.")
  topping_out = "None"
else:
  if topping == 1:
    price += 2
    topping_out = "Pepperoni"
  elif topping == 2:
    price += 1.5
    topping_out = "Mushrooms"
  elif topping == 3:
    price += 1
    topping_out = "Onions"
  elif topping == 4:
    price += 1.75
    topping_out = "Extra Cheese"

#ask the user if they want to see the order summary here
choice = input("Would you like to see your order summary (y or yes)? ").lower()
if choice == 'y' or choice == 'yes':
  orderSummary()

print("\nAvailable Drinks:")
print("1. Soda ($2) \n2. Water ($1)")
drink = int(input("\nChoose one drink (1/2): "))
if drink > 2 or drink < 1:
  print("\nInvalid Choice\nRe-run the program for a drink")
  drink_out = "None"
else:
  if drink == 1:
    price += 2
    drink_out = "Soda"
  elif drink == 2:
    price += 1
    drink_out = "Water"

#ask the user if they want to see the order summary here
choice = input("Would you like to see your order summary (y or yes)? ").lower()
if choice == 'y' or choice == 'yes':
  orderSummary()

