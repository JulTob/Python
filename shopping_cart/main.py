'''
SHOPPING CART
Julio Toboso
Basic program for a SHOPPING CART.
Practice for coding.
'''
from IPython.display import clear_output

# Cart List #
cart = []
# --------- #

#Cart Functionalities #

## Add Item ##
def addItem(item):
    clear_output()
    cart.append(item)
    print(f"✅ {item} has been added.")

## Remove ##
def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print(f"❌ {item} has been removed.")
    except:
        print(f"⁉️  Sorry, we couldn't remove {item} from the card. Are you shure it's there?")

## Print_Cart ##
def showCart():
    clear_output()
    if cart:
        print("🛒 Shopping Cart:")
        for item in cart:
            print(f"\t 🛍  - {item}")
    else:
        print("🛒 Your cart is empty.")

## Clear Cart ##
def clearCart():
    clear_output()
    cart.clear()
    print("♻️  Your cart is now empty.")

'''test
addItem("Stuff")
addItem("Stuff")
removeItem("Stuff")
removeItem("OtherStuff")
showCart()
clearCart()
showCart()
'''

# Main #
def main():
    end = False
    while not end:
        option = input("""\
     ⛔️ Quit
     ➕ Add
     ➖ Remove
     📃 Show
     🆑 Clear \n""").lower()
        if option == "quit":
            end = True
        elif option == "add":
            item = input("❔ What Item? ")
            addItem(item)
        elif option == "remove":
            item = input("❔ What Item? ")
            removeItem(item)
        elif option == "show":
            showCart()
        elif option == "clear":
            clearCart()

main()
