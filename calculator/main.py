'''
CALCULATOR

Julio Toboso

Basic program for algebraic calculations.
Practice for coding basic documents.

'''

print(''' Welcome!
You can do the next operations:
    1. Add      \t(+)
    2. Substract\t(-)
    3. Multiply \t(*)
    4. Divide   \t(/)
    5. Result   \t(=)

They resolve by First in First out (Polish Notation).
''')
result = float(input("Operation\tOperands:\n\t\t"))
# Determine Calculation #
operate = True
while operate:
    try:
        operation = input(f"{result}\t").lower()
    except:
        operation = "?"
    if operation=="add" or operation=="+" or operation=="1":
        variable = float(input("\t\t"))
        result += variable
    elif operation=="substract" or operation=="-" or operation=="2":
        variable = float(input("\t\t"))
        result -= variable
    elif operation=="multiply" or operation=="*" or operation=="3":
        variable = float(input("\t\t"))
        result *= variable
    elif operation=="divide" or operation=="/" or operation=="4":
        variable = float(input("\t\t"))
        try:
            result /= variable
        except:
            operate = False
            print("NaN")
    elif operation=="result" or operation=="=" or operation=="5" or operation=="":
        operate = False
    else:
        print(f"{operation}?\t")



#-------------#
print("\t =  " + str(result))
