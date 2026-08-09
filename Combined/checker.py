inventory = {"apple": 10, "banana": 5, "milk": 0} # product: stock

while True:
    product = input("Enter product name to buy or 'exit' to stop: ").lower()
    
    if product == "exit":
        break
    
    if product in inventory:
        if inventory[product] > 0:
            inventory[product] -= 1
            print(f"{product} purchased. Stock left: {inventory[product]}")
        else:
            print("Out of Stock")
    else:
        print("Product not found")

print("Final Inventory:", inventory)