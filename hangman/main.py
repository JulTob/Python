'''
HANGMAN
Julio Toboso
Basic program for hangman game.
Practice for coding games.
'''

# Imports #
from random import choice
#---------#

# Game Preparation #
words = ["Code", "Computer", "User", "Penguin"]
word = choice(words).lower()
lifes = 5
## Guessed leters ##
guessed = ["*"]*len(word)
#-------------#


# Get Guess #
def guess():
    letter = input("Choose a letter: ")
    if len(letter)>1:
        print("Only one character")
        letter = guess()
    if not letter.isalpha():
        print("Alphabetic characters only")
        letter = guess()
    return letter.lower()
#-------------#

# Bye message #
congratulations = "Yeah! That's it! the word is " + word
game_over = "No! You lost! The word is " + word
# ------------#

# Main loop #
end = False
while not end:
    print('|'.join(guessed))
    l = guess()
    if l in word:
        for c in range(len(word)):
            if word[c]==l:
                guessed[c] = l
    else:
        lifes -= 1
    if lifes <= 0:
        end = True
        print(game_over)
    if "*" not in guessed:
        end = True
        print(congratulations)
