# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for s in secretWord:
       if s not in lettersGuessed:
           return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s_len = len(secretWord)
    str_output = ''
    for i in range(s_len):
        if secretWord[i] in lettersGuessed:
            str_output += secretWord[i]
        else:
            str_output += '_ '

    return str_output


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    str_a = string.ascii_lowercase
    for l in lettersGuessed:
        str_a = str_a.replace(l, '')
        
    return str_a

def guess_result(l, secretWord, availableLettters,lettersGuessed):
    
    guessedWord = getGuessedWord(secretWord, lettersGuessed)
    
    if l in secretWord and l in availableLettters:
        return 'Good guess: '+ guessedWord
    elif l in secretWord and l not in availableLettters:
        return "Oops! You've already guessed that letter:" + guessedWord
    elif l not in secretWord and l not in availableLettters:
        return 'Oops! invalid guess:  ' + guessedWord 
    else:
        return 'Oops! That letter is not in my word:'+ guessedWord
    
   
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    
    You have 1 guesses left.
	Available Letters: ijklmnopqrstuvwxyz
	Please guess a letter: i
	Oops! That letter is not in my word: e_ _ e
	-----------
	Sorry, you ran out of guesses. The word was else. 
          
    
    '''
    # FILL IN YOUR CODE HERE..
    s_len = len(secretWord)
    lettersGuessed = []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ', s_len, ' letters long.')
    print('- '*10)
    guesses = 12
    while guesses > 0:
        print('You have ',guesses, ' guesses left.')
        availableLetters = getAvailableLetters(lettersGuessed)        
        print('Available Letters: ', availableLetters)
        l = input('Please enter a letter: ').lower()
        lettersGuessed.append(l)
        print(guess_result(l, secretWord, availableLetters,lettersGuessed))
        print('- '*10)
        guesses -= 1
        
        re = getGuessedWord(secretWord, lettersGuessed)
        
        if re == secretWord:
            print ('Congratulations, you won!')
            
    print('Sorry, you ran out of guesses. The word was', secretWord)
        
        
        
        
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
