'''
SHOPPING CART
Julio Toboso
Basic program for a SHOPPING CART.
Practice for coding.
'''
from IPython.display import clear_output

# Cart Object API #
class Cart:
    def __init__(self):
        self.cart = []

    # Cart Functionalities #

    ## Add Item ##
    def addItem(self,item):
        clear_output()
        self.cart.append(item)
        print(f"✅ {item} has been added.")

    ## Remove ##
    def removeItem(self,item):
        clear_output()
        try:
            cart.remove(item)
            print(f"❌ {item} has been removed.")
        except:
            print(f"⁉️  Sorry, we couldn't remove {item} from the card. Are you shure it's there?")

    ## Print_Cart ##
    def showCart(self):
        clear_output()
        if self.cart:
            print("🛒 Shopping self.cart:")
            for item in self.cart:
                print(f"\t 🛍  - {item}")
        else:
            print("🛒 Your cart is empty.")

    ## Clear Cart ##
    def clearCart(self):
        clear_output()
        self.cart.clear()
        print("♻️  Your cart is now empty.")

    def menu(self):
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
                self.addItem(item)
            elif option == "remove":
                item = input("❔ What Item? ")
                self.removeItem(item)
            elif option == "show":
                self.showCart()
            elif option == "clear":
                self.clearCart()
            else:
                print("")

# --------- #

my_cart = Cart()
my_cart.addItem("Stuff")
my_cart.addItem("Stuff")
my_cart.removeItem("Stuff")
my_cart.removeItem("OtherStuff")
my_cart.showCart()
my_cart.clearCart()
my_cart.showCart()


# Main #

my_cart.menu()
