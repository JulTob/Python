
'''
BILLING PRINTER

Julio Toboso

Basic program for printing bills for a business.
Practice for coding basic documents.

'''

# Busines information #
company_name = "Coding Business S.A."
company_address = "27º C/Miguel Hernandez"
company_city = "03300 Orihuela(Alicante)"
company_country = "Spain"
#-------------#


# Product list #
p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 699.99
p3_name, p3_price = "Mouse", 9.95
#-------------#

# Bye message #
bye = "Thanks for shopping with us!"


# Beggining of document #
## Separator ##
print("*" * 50)

## Company info ##
print(f"\t{company_name.title()}")
print(f"\t{company_address.title()}")
print(f"\t{company_city.title()}")
print(f"\t{company_country.upper()}")

## Separator ##
print("=" * 50)

## List of products ##
print('''\tProduct \tPrice''')
print("_" * 50)
print(f"\t{p1_name.title()}    \t€{p1_price}")
print(f"\t{p2_name.title()}    \t€{p2_price}")
print(f"\t{p3_name.title()}    \t€{p3_price}")

## Separator ##
print("=" * 50)

## Total Price ##
total = p1_price + p2_price + p3_price
print("\t\tTotal")
print(f"\t\t{round(total,2)}")

## Separator ##
print("=" * 50)

## Bye
print('\n\t' + bye + '\n' )

## Separator ##
print("*" * 50)


'''

fof n in List:
	print(f"	{Product[n]}		{Price[n]}")
print("="*15)
print(f"	Total		{total}")
print("="*15)
print("Thanks for shopping here!")
print("*"*15)
'''
