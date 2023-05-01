# Programming 2 
# Jonah Labeda 2B.

# The Hangman List that draws the hang man when guesses are wrong

from random import randint
HANGMAN = [
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
"""]

MAX_WRONG = len(HANGMAN) - 1
WORDS = ["PYTHON", "PROGRAMMING", "GUESS", "CODE", "COMPILE", "BUG", "KITTEN", "RISE", "OF", "KINGDOMS", "RISEOFKINGDOMS", "AMOGUS", "CAN", "MOM", "DAD", "MILK"] #words to guess -- enter your own words here (10)
something = randint(0,len(WORDS)-1)
# initialize variables
# the word to be guessed
word = WORDS[something]                # replace this to pick a random word from the list.
so_far = ["-"] * len(word)      # one dash for each letter in word to be guessed
wrong = 0                       # number of wrong guesses player has made
used = []                       # letters already guessed
word = list(word)               # turns chosen word into a list
length = len(word)
#print(word)
print("Welcome to Hangman.    Good luck!") #opening statement
print("HINT:  The word is", "_"*length, "letters long.")       # clues user to word length 
print(HANGMAN[wrong])



while wrong < MAX_WRONG and so_far != word:
  guess = input("\n\nEnter your guess: ")  #tell user to guess a word
  guess = guess.upper()
  if len(guess) == 1:
    used += guess
    used.sort()
  for i in range(len(word)):
    if guess == word[i]:
      so_far.pop(i)
      so_far.insert(i, guess)
    
    # continue to ask the user for the guess if the guess is in the used list.
    
    # add the guess onto the used letter list. 
  guesslist = []
  finalWord = ""
  if len(guess) != 1:
    for i in guess:
      guesslist += i
  if guesslist == word:
    so_far = word
    print("You got it!! :)")
    print("The word was: ",*so_far, sep="")
  if len(guess) == 1:
    for i in range(len(so_far)):
      if so_far == word:
        print("You got it!! :)")
        print("The word was: ",*so_far, sep = "")
        break
  if so_far == word:
    break
    # check to see if the guess is in the word, if so then go through the list and 
    #if so_far == word:
      #break
    # replace each occurence of the letter in the so_far list. 
  if guess not in word:
    wrong += 1
    
    if wrong == 7:
      print("YOU LOSE!!! (^-° )")
      print("The word was: ",*word, sep = "")
      print(HANGMAN[wrong])
      break
    print(HANGMAN[wrong])

    





    
   
    # otherwise:  Tell the user the letter isn't in the word, increase number wrong, display the new HANGMAN
    
  print("\nYou've used the following letters:\n", *used, sep = " ")
  print("\nSo far, the word is:\n", *so_far, sep = " ")  

# after the loop is over:
# if they didn't guess it tell them what it was, otherwise tell them you guessed it. 



