""" Short, one line description of the module ending with a period.
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Your Name"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "your.address@education.nsw.com.au"
__status__ = "Prototype, Development or Production"

#dependencies


       
#define other setup variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
correctGuesses = "-" * len(vowels)
remainingGuesses = 10

#setup game
print("DO YOU KNOW YOUR VOWELS?")

#game loop
while remainingGuesses > 0:
    print("your correct guesses so far:\n")
    print(correctGuesses+"\n")
    print("you have {} guesses left\n".format(remainingGuesses))
    print(alphabet+"\n")
    guess = input("pick a letter that you think is a vowel, or Q to quit: ")
    
    #check to see if the player wants to quit
    if guess == "Q":
        print("dumb or just chicken? thanks for playing")
        remainingGuesses = 0
        
    #otherwise play the game
    elif guess in alphabet:  #check the player has selected an unused letter
        alphabet = alphabet.replace(guess, "-") #remove the letter from available guesses
        
        if guess in vowels: #check to see if the guess is a vowel
            #now we have to find the index of the letter so we can replace it
            for i in range(0, len(vowels)):
                if guess == vowels[i]:
                    print("Correct!\n")
                    #place the letter in the correct position in the correct guesses string
                    correctGuesses = correctGuesses[:i] + guess + correctGuesses[i+1:]
                    #next check to see if all the vowels have been guessed
                    if correctGuesses == vowels:
                        print("\n WINNER! - Wow! Look who pain attention in Kindy!")
                        remainingGuesses = 0 #player has won so need to exit loop
        
        else: #the guess was incorrect
            remainingGuesses = remainingGuesses - 1
            if remainingGuesses == 0: #all guesses have been used up
                print("seriously you loser...did you even go to kindy?")

    else: #the player did not choose a valid letter
        print("\nthat was a dumb guess you moron...try again \n")
