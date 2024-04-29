# Hangman first 4/28
import random
print('welcome to the end')
print("--------------------------")

wordDictionary = ('Elephant, Rainbow, Computer, Butterfly, Chocolate, Adventure, Guitar, Sunshine, Backpack, Fireworks, Dragon, Ocean, Moonlight, Pizza, Galaxy, Watermelon, Telescope, Happiness, Umbrella, Bicycle, Kangaroo, Sandwich, Symphony, Lemonade, Jellyfish')

######choose a random word
randomWord = random.choice(wordDictionary)

for x in randomWord
    print("_", end=' ')

    def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1):
        print("\n+---+")
        print(" O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print(" O    |")
        print(" |   |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O   |")
        print("/|   |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O   |")
        print("/|\   |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("   ===")
    elif(wrong == 6):
        print(" O   |")
        print("/|\  |")
        print("/ \   |")
        print("   ===")

def printWord(guessedLetter):
    counter=0
    rightLetter=0
        for char in randomWord:
            if(char in guessedLetter):
                print(randomWord[counter],end=" ")
                rightLetters+=1 
            else:
                print(" ",end="")
                counter+=1 
            return rightLetter
    

    def printLines():
        print("\r")
        for char in randomWord:
            print("\u203",end="")