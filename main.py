#Hangman
from time import sleep
import random
from hangman_parts import parts

class Game:
    def __init__(self, word):
        self.word = word
        self.guesses_left = 6
        self.right_guesses = ['_'] * len(word) 
        self.wrong_guesses = [] 

#Prints a hangman picture
print("Welcome to Hangman")
print('   ',  '------')
print('   ',  '|    |')
print('   ',  '|    O')
print('   ',  '|   -|-')
print('   ',  '|    |')
print('   ',  '|   / \\')
print('------------')

print('Let me think of a word')

#Wait time function
def wait():
    for i in range(5):
        print('.', end = "")
        sleep(.2)
    print()
    
wait()

#List of words
file = open("words.txt", "r")
  
# reading the file
data = file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
words = data.split("\n")
file.close()

# creating an instance of a Game class  
game = Game(random.choice(words)) 

print("Okay I've got it!")

print("The word has", len(game.word), "letters")

for i in range(len(game.word)):
    print('_',' ', end = "")
    
print()

#Prints letters in right with _'s
def add_letter():
    for i in game.right_guesses:
        print(i, ' ', end = "")
    print()

#Prints out wrong letters
def wrong_letter():
    print("Wrong letters: ", end = "")
    for i in game.wrong_guesses:
        print(i,' ',end = "")
    print()

#Main Loop        
while True:
    print('=====================')
    if game.guesses_left > 1:
        print("You have", game.guesses_left, "mistakes left.")
    else:
        print("You have", game.guesses_left, "mistake left.")
    guess = input("Guess a letter: ")
    if guess in game.word:
        print("Let me check")

        ###Handles letter that appear more than once
        index = 0
        for i in game.word:
            if i == guess:
                game.right_guesses[index] = guess
            index = index + 1

        wait()
        add_letter()
        wrong_letter()
        parts(len(game.wrong_guesses))
        
    elif guess not in game.word:
        print("Let me check")
        wait()
        if guess in game.wrong_guesses:
            print("You already guessed", guess)
            wrong_letter()
        else:
            print(guess, "is not in my word")
            game.wrong_guesses.append(guess)
            game.guesses_left -= 1
            add_letter()
            wrong_letter()
            parts(len(game.wrong_guesses))
            
    if len(game.wrong_guesses) == 6:
        print("Game Over!")
        print("I picked", game.word)
        break
    
    if '_' not in game.right_guesses:
        print("You guessed it!")
        print("I picked", game.word)
        break

# https://www.mrmichaelsclass.com/python-programming/python-projects/hangman
