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
import pygame as P # accesses pygame files
import random as R #so we can use random selection and placement
import sys  # to communicate with windows


# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 800, 600  # sets size of screen/window
screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen

# set variables for some colours RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


#define necessary classes
class Sprite(object): #the images will be rendered as sprites
    """southpark sprites.

    Create a sprite with necessary parameters to draw it

    Attributes:
        screen_size: the size of the display screen in pixels

    """

    def __init__(self, imageFilename):
        """Initiates the properties of the sprite."""
        self.image = P.image.load(imageFilename)
        #uncomment the line below if you want to scale the image
        #self.image = P.transform.scale(self.image,(100,500))
        self.rectangle = self.image.get_rect()
        self.set_position()

    def set_position(self):
        """ creates a fixed position for sprite on the screen.
        """        
        self.rectangle.left = 300
        self.rectangle.top = 100

#other setup stuff
imageFilenames = ["media/kenny.png",
                  "media/cartman.png",
                  "media/kyle.png",
                  "media/stan.png",
                  "media/kenny_dead.png"]

#render the images and put them into an array
spriteArray = [] #start with empty array
for filename in imageFilenames:
    newSprite = Sprite(filename) #makes the sprite
    spriteArray.append(newSprite) #adds it to the array
    
#clear the screen
screen.fill(blue) #this sets the background colour
    
spriteIndex = 0
play = True  # controls whether to keep playing



# game loop - runs loopRate times a second!
while play:  # game loop - note:  everything in this loop is indented one tab

    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
    # your code starts here ##############################
    
    #check to see if the user presses the mouse button down,
        elif event.type == P.MOUSEBUTTONDOWN:
            if spriteIndex >= len(spriteArray): #no sprites left
                pass
        
            else:
                thisSprite = spriteArray[spriteIndex]
                screen.fill(blue) #clear screen & set the background colour

                screen.blit(thisSprite.image, thisSprite.rectangle)
                spriteIndex += 1


    # your code ends here ###############################

    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop ###############
print("Thanks for playing")  # notifies user the game has ended
P.quit()   # stops the game engine
sys.exit()  # close operating system window
