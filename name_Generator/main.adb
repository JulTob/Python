import sys, random

print("Welcome to Superhero Namer. \n")

first = (
"Super", "Spider", "Bat", "Wonder", "Green",
"Martian", "Magic", "Animal", "Atom"
)

last = (
"Man", "Woman", "Kid", "Hero", "Hunter", "Guardian"
)

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print("\n\n")
    print(f"{firstName}{lastName}", file=sys.stderr)
    print("\n\n")

    again = input("Try again? ([n] to quit)\n")
    if again.lower() == 'n':
        break
