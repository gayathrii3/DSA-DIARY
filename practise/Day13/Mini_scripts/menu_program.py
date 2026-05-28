menu = {"chicken peri-peri" : 599,
        "chicken wings" : 499,
        "nuggets" : 299,
        "coco-cola" : 79,
        "fries" : 129}

cart = []
total = 0

print("============MENU===========")

for key, value in menu.items():
    print(f"{key:18} = \u20B9{value}")

print("---------------------------")

while True:
    food = input("Select the food item(q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("========Your order=========")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()

print(f"Total is \u20B9{total}")







