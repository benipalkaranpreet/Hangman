# Hangman Game in Python
# Karanpreet Benipal
# Made on July 24th, 2022

import linecache;
import random;

lettersGuessed = [];
lives = 5;
# this is the relative path to the .txt file containing the list of phrases or words used in the game
wordFile = 'words.txt'; 

def genWord():
    wordList = open('words.txt', 'r');
    
    # Count the number of lines in the file 
    count = sum(1 for line in open(wordFile));
    
    # Pick a random line to use as the phrase
    gen = linecache.getline(wordFile, random.randint(1, count))
    return gen.strip();

# Generate the word
word = genWord();

def checkGame(): 
    print("===================================================================================================")
    won = True;
    for x in range(len(word)):
        if word[x] in lettersGuessed:
           print(word[x] + " ", end ='');
        else: 
            print("_ ", end ='');
            won = False;
    print("")
    
    print("You have %d incorrect guess(es) left" % lives)
    print("The letters you have guessed are: ", end='')
    print(lettersGuessed)
    return won;

    

#Play the Game:

while True:
    if lives < 0:
        print("YOU LOSE")
        print("The correct answer was: ", word)
        break;

    if checkGame():
        print("Winner!!!")
        break;

    guess = input("Guess a letter: ");
    lettersGuessed.append(guess);
  
    if not guess in word:
         lives -= 1;

