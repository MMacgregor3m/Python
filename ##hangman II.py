##hangman II
import random

animals=['cat','dog','shark','bird','rhino','tiger','lion']
word = random.choice(animals).lower()

guessed_correctly = []
guessed_incorrectly = []
tries = 6
hangman_count=-1
while tries > 0:
    output = ''
    for letter in word:
        if letter in guessed_correctly
            output += letter
    else:
        output += '_ '
