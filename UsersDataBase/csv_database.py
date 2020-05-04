'''
Database example program
Based on CSV

Julio Toboso

'''


# Dependencies
import csv
from IPython.display import clear_output


''' User Registration '''
def registerUser():
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f,delimiter=",")
        print("👤 Introduce your Info.")
        email = input("📧 E-Mail: ")
        password = input("🔏 Introduce a Password: ")
        password_confirm = input("🔏🔍 Introduce the Password again: ")
        clear_output()
        if password == password_confirm:
            writer.writerow([email,password])
            print("✔ Registration success")
        else:
            print("❌ Registration error: Password incongruency")

''' User Access Log In '''
def loginUser():
    try:
        print("👥 To Log In, introduce your data: ")
        email = input("📧 E-Mail: ")
        password = input("🔏 Password: ")
        clear_output()
        with open("users.csv", mode = "r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if row == [email, password]:
                    print("🕶 You logged IN")
                    return True
        print("❌ LogIn error.")
        return False
    except:
        print("❌ LogIn error.")
        return False

def main():
    active = True
    logged_in = False
    # main loop
    while active:
        if logged_in:
            print('''\
    1. 🔳 LogOut
    0. 🔘 Quit
            ''')
        else:
            print('''\
    1. 🔲 LogIn
    2. ➕ Register
    0. 🔘 Quit
            ''')
        selection = input("What action would you like to do?  ").lower()
        print(selection)
        clear_output()
        if ( selection == "register" or selection == "2") and logged_in == False:
            registerUser()
        elif ( selection == "login" or selection == "1") and logged_in == False:
            logged_in = loginUser()
        elif ( selection == "quit" or selection == "0"):
            active = False
            print("👋 Bye!")
        else:
            print("❔❔❔ Can you try again?")
main()
