# shopping cart in python
# starter file

# ?? your name(s) here

inventory = {'Pencil': 0.25, 'Soda': 1.00, 'Mug': 3.00}  #  ?? add the dictionary values for items available for sale



#main starts here
def main():
    cart = {}
    done = False
    while not done:

        showItems()
        choice = input("1 - Add Item, 2 = Remove Item, q = Quit: ")

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



def showItems():
     print("Items available:")
     for key, val in inventory.items():
         print(key, val, end = "")
         print()
     # print the keys from your inventory dictionary to show the items  available for sale
     # ??

def addItem(cart, itemToAdd, quantity):
        # if an item is in the cart already, increase the quantity by the number to add
        # otherwise add the quantity specified then return the value of cart
        # ??
    dictionarykeys = inventory.keys()
    if len(cart) != 0:
        for item in cart:
            if cart[itemToAdd] != 0:
                cart += quantity
                # add 1
            elif cart[itemToAdd] != 0:
                cart += quantity
                # add 1
            elif cart[itemToAdd] != 0:
                cart += quantity
            else:
                break

    else:
        # add the items from itemToAdd into cart
        return cart


        # pass


def delItem(cart, itemToRemove, quantToRemove):
    # if the item to remove is in the cart, remove the specified quantity
    # if there are not enough in the cart to remove,
    #    leave the cart unchanged and display an error message
    # return the cart
    # ??
    pass

def printCart(cart):
    # print each item in the cart, the quantity of each, and the cost of that many items
    # be sure to format costs as $ with two decimals
    print("Your Cart:")
    # ??

def totalCart(cart):
    # calculate and return the total cost of all items in the cart
    pass


main()
