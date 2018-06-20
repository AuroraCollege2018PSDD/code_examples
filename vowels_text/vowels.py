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
play = True

#setup game
print("DO YOU KNOW YOUR VOWELS?")

#game loop
while remainingGuesses > 0:
    print("your correct guesses so far:\n")
    print(correctGuesses+"\n")
    print("you have {} guesses left\n".format(remainingGuesses))
    print(alphabet+"\n")
    guess = input("pick a letter that you think is a vowel, or Q to quit: ")
    if guess == "Q":
        print("dumb or just chicken? thanks for playing")
        remainingGuesses = 0
    elif guess in alphabet:
        alphabet = alphabet.replace(guess, "-")
        if guess in vowels:
            for i in range(0, len(vowels)):
                if guess == vowels[i]:
                    print("Correct!\n")
                    correctGuesses = correctGuesses[:i] + guess + correctGuesses[i+1:]
                    if correctGuesses == vowels:
                        print("\n WINNER! - Wow! Look who pain attention in Kindy!")
                        remainingGuesses = 0
        else:
            remainingGuesses = remainingGuesses - 1
            if remainingGuesses == 0:
                print("seriously you loser...did you even go to kindy?")

    else:
        print("\nthat was a dumb guess you moron...try again \n")
