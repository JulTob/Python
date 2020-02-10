'''
GUESSING GAME
_____________

Julio Toboso

Standard guessin game for beginers to code.

You give a number, if it is the one, you win.
'''

from random import randint
from IPython.display import clear_output

guessed = False
number = randint(0,100)
guesses = 0
while not guessed:
    ans = input("Try to guess the number I'm thinking: ")
    guesses += 1
    clear_output()
    if int(ans) == number:
        print("That's right!")
        print("It only took {} guesses!".format(guesses) )
        break
    elif int(ans) > number:
        print("Too high")
    elif int(ans) < number:
        print("Too low")
