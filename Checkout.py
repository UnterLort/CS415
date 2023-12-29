# @Kyle Stewart @Checkout.py version 1
# This makes an empty list and a variable to track the list total cost
items = []
total = 0.0

print("Welcome to 415-Mart!")

# Starts a while loop
while True:

    print("Please enter an item to purchase.")
    item = str(input())
    # If the item is Done the loop will print out the list and then stop the loop
    if item == "Done":
        print("-" * 10)
        print("Receipt:")
        # The for loop will organize and print the item and the cost of each
        for shop in items:
            item, cost = shop
            # Prints the item then 8 spaces then the cost of it
            # Then keeps going till all item and cost is listed
            print(f"{item:8s} ${cost:.2f}")
        # Prints the cost of all items together
        print(f"Total: ${total:.2f}")
        break
        # Ends the loop
    else:
        # If not "Done" will ask for the cost of the item by the user
        print("Please enter the cost of this item.")
        cost = float(input())
        # Adds the item and cost to the items list
        items.append((item, cost))
        # Adds the cost above to the total
        total += cost
