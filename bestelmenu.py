# Simple Food Ordering Menu

# Menu dictionary
menu = {
    "pizza": 8.50,
    "pasta": 7.00,
    "salad": 5.50,
    "soup": 4.00
}

# Show the menu
print("---- MENU ----")
for item in menu:
    print(item, "-", "€" + str(menu[item]))
print("--------------")

# Take the order
order = {}
while True:
    choice = input("What would you like to order? ").lower()
    if choice == "done":
        break
    if choice in menu:
        if choice in order:
            order[choice] += 1
        else:
            order[choice] = 1
    else:
        print(f"'{choice}' is not on the menu!")

# Print the receipt
print("\n--- RECEIPT ---")
total = 0
for item in order:
    price = menu[item] * order[item]
    total += price
    print(item, "x" + str(order[item]), "-", "€" + str(price))
print("Total: €" + str(total))
