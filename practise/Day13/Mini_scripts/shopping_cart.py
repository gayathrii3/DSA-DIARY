your_items = []
prices = []
total = 0

name = input("Enter your name: ")
print(f"----------Welcome {name}----------")

while True:
    stuff = input("Pick your items(q to quit): ")
    if stuff == 'q':
        break
    else:
        price = float(input(f"Enter the price of {stuff}: \u20B9"))
        your_items.append(stuff)
        prices.append(price)

print("---------Your order---------")

for stuff in your_items:
    print(stuff,end= ", ")
print()

for price in prices:
    total += price

print(f"Your total is : \u20B9{total}")


