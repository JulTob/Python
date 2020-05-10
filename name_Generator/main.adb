"""Superhero name generator!!!

Selects two names to combine them into a superhero name.
"""

import sys
import random

def main():
    """Choose names at random from 2 tuples of names
    and print the result"""
    print("Welcome to Superhero Namer. \n")

    first = (
    "Super", "Spider", "Bat", "Wonder", "Green",
    "Martian", "Magic", "Animal", "Atomic", "Fire",
    "Elastic", "Invisible", "Rock", "Tiguer", "Iron",
    "Night", "Galactic", "Space", "Electric", "Fantom"
    )

    last = (
    "Man", "Woman", "Kid", "Hero", "Hunter", "Guardian",
    "Racoon", "Fist", "Devil", "Storm", "Ghost", "Rider"
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

if __name__ == "__main__":
    main()
