"""
A dictionary which increases/decreases values of items in your
shopping cart based on user inputs
"""

inventory = {"pencil":0.25,"soda":1,"mug":3}  #  ?? add the dictionary values for items available for sale

def showItems():
     print("Items available:", end =" ")
     for key in inventory.keys():
         print(key, end=" ")

def addItem(cart, itemToAdd, quantity):
    if itemToAdd not in inventory.keys():
      print(f"Error, item not in inventory. Please choose pencil, soda or mug.")
      return cart
    else:
      if itemToAdd in cart:
          cart[itemToAdd] += quantity
      else:
          cart[itemToAdd] = quantity
      return cart

def delItem(cart, itemToRemove, quantToRemove):
    if itemToRemove not in cart:
        print(f"Error. Item not in cart.")
    elif quantToRemove <= cart[itemToRemove]:
        cart[itemToRemove] -= quantToRemove
    else:
        print(f"Error: you don't have that many {itemToRemove} in your cart.")
    return cart

def printCart(cart):
    print("Your Cart:")
    for (key, val) in cart.items():
        print(f"{key:12s}{val:<12d}${val*inventory[key]:5.2f}")

def totalCart(cart):
    total = 0
    for key, val in cart.items():
        total += val*inventory[key]
    return total

def main():
    cart = {}
    done = False
    while not done:

        showItems()
        choice = input("1 - Add Item, 2 = Remove Item, q = Quit: " )

        if choice == "1":
            itemToAdd = input("Enter item to add:")
            quantity = int(input("Quantity to add:"))
            cart = addItem(cart, itemToAdd, quantity)
            printCart(cart)
        elif choice == "2":
            itemToDelete = input("Enter item to remove:")
            quantity = int(input("Quantity to remove:"))
            cart = delItem(cart, itemToDelete, quantity)
            printCart(cart)
        elif choice.lower() == "q":
            done = True

    print("----")
    printCart(cart)
    total = totalCart(cart)
    print(f"Total order is: ${total:>5.2f}")

main()
