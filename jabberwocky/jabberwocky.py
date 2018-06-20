""" Short, one line description of the module ending with a period.
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Your Name"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "your.address@education.nsw.com.au"
__status__ = "Prototype, Development or Production"



#open the text file with error handling
try:
    inputFile = open('jabberwocky.txt', 'r')
    outputText = inputFile.read()
    inputFile = open('jabberwocky.txt', 'r')
    textArray = inputFile.readlines() #read the file
    inputFile.close() #always good practice to close the file ASAP
    
except IOError: #if there was an error trying to open the file
    print("bugger I cant find the file")
    SystemExit() #close python and exit
    
    
choice = input('Would you like to print a line (L), word (w) or letter(l) or any other key to exit: ')

if choice in 'Lwl':
    lineChoice = int(input('enter the line number: '))
    print(len(textArray))
    if lineChoice >= len(textArray): #invalid choice
        print("Invalid line choice")
        print("the text is")
        print(outputText)
        choice = "q"
    else:
        outputText = textArray[lineChoice - 1]


    if choice in 'wl':
        wordChoice = int(input('enter the word number: '))
        wordArray = outputText.split() #split the line into separate words
        if wordChoice >= len(wordArray):
            print("Invalid word choice")
            print("the line is")
            print(outputText)
            choice = 'q'
        else:
            outputText = wordArray[wordChoice - 1]
        
        
        if choice == 'l':
            letterChoice = int(input('enter the letter number: '))
            if letterChoice >= len(outputText):
                print("Invalid letter choice")
                print("the word is")
                print(outputText)
            else:
                outputText = outputText[letterChoice - 1]
                
else:
    outputText = 'thanks for playing, Doofus'
    
print(outputText)