# Hangman first 4/28
import random
print("Welcome to your end")
print("--------------------------")

wordDictionary = ('Elephant, Rainbow, Computer, Butterfly, Chocolate, Adventure, Guitar, Sunshine, Backpack, Fireworks,Dragon, Ocean, Moonlight, Pizza, Galaxy, Watermelon, Telescope, Happiness, Umbrella, Bicycle, Kangaroo, Sandwich, Symphony, Lemonade, Jellyfish')

######choose a random word
randomWord = random.choice(wordDictionary)

for x in randomWord:
    print("_", end=" ")

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
        print("     |")
        print("     |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print(" O   |")
        print(" |   |")
        print("     |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("     |")
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
        print("/ \  |")
        print("   ===")

def printWord(guessedLetters):
    counter=0
    rightLetters=0
    for char in randomWord:
            if(char in guessedLetters):
                print(randomWord[counter],end=" ")
                rightLetters+=1 
            else:
                print(" ",end="")
                counter+=1 
            return rightLetters
    

    def printLines():
        print("\r") 
        for char in randomWord:
            print("\u203e",end="")

            length_of_word_to_guess = len(randomWord)
            amount_of_times_wrong = 0
            current_guess_index = 0
            current_letters_guessed = []
            current_letters_right = 0

            while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
                print("\nLetters guess so far: " )
                for letter in current_letters_guessed:
                    print(letter, end=" ")
            ##Prompt user for imput
            letterGuessed = input("\nGuess a letter:")
            ###User is right
            if(randomWord[current_guess_index] == letterGuessed):
                print_hangman(amount_of_times_wrong)
                ###Print Word
                current_guess_index+=1
                current_letters_guessed.append(letterGuessed)
                current_letters_right=printWord(current_letters_guessed)
                printLines
                ###User was wrong af
            else:
                amount_of_times_wrong+=1
                current_letters_guessed.append(letterGuessed)
                ###update drawing
                print_hangman(amount_of_times_wrong)
                ###print word
                current_letters_right = printWord(current_letters_guessed)
                printLines()

                print("Game Over, you live another day")       