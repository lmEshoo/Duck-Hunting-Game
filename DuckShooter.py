# Lini Mestar
# Duck Hunting game v1.0
# big thanks to all the resources I found
# that helped me write this program (game)


## os is used for environment variables to set the position to center
import pygame, sys, random, os
from pygame.locals import *

def initPyGame():
	
	## initializes all pygame locals
	pygame.init()
	
	os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

	pygame.display.set_caption("Duck Hunt v1.0")

	pygame.mouse.set_visible(False)

class backgroundClass():
	## This class contains properties and methods for our background
	
	def __init__(myBackground):
		backgroundFile = "background.jpg"
		myBackground.image = pygame.image.load(backgroundFile).convert()	
		
	def draw(myBackground):
		screen.blit(myBackground.image, (0,0))

class aimClass(pygame.sprite.Sprite):
	def __init__(myAim):
	   ## Initialize a sprite, passing this instance as a parameter
	   pygame.sprite.Sprite.__init__(myAim)
	   aimFile = "aim.png"
	   myAim.image = pygame.image.load(aimFile).convert_alpha()
	   myAim.rect = myAim.image.get_rect()
	   
	def update(myAim):
		## Move the crosshairs to where the mouse is
		position = pygame.mouse.get_pos()
		myAim.rect.center = position
		
class duckClass(pygame.sprite.Sprite):
	def __init__(myDuck, startPos, speed):
	   ## Initialize a sprite, passing this instance as a parameter
	   pygame.sprite.Sprite.__init__(myDuck)
	   duckFile = "target.gif"
	   myDuck.image = pygame.image.load(duckFile).convert_alpha()
	   myDuck.rect = myDuck.image.get_rect()
	   myDuck.rect.right = 0
	   myDuck.rect.centery = startPos
	   myDuck.duckSpeed = speed
	   
	def update(myDuck):
		myDuck.rect.right += myDuck.duckSpeed
		screenRect = screen.get_rect()
		
		if myDuck.rect.left >= screenRect.right:
			myDuck.rect.right = 0
			myDuck.rect.top = myDuck.randomYValue(screenRect)
			
	def randomYValue(myDuck, screenRect):
		startRange = myDuck.rect.height
		endRange = screenRect.height - myDuck.rect.height
		randomY = random.randrange(startRange, endRange)
		return randomY
		
class scoreClass:
	## Class to hold the score and update the score to the screen

	def __init__(myScore):
		myScore.value = 0
		myScore.font = pygame.font.Font(None, 36)
		
	def update(myScore):
		## Font.renderer(text, fontSmoothing, colour(r, g, b))
		text = myScore.font.render("Score: %s" % myScore.value, True, (0, 0, 0))
		textRect = text.get_rect()
		screenRect = screen.get_rect()
		textRect.centerx = screenRect.width - textRect.width
		screen.blit(text, textRect)
		
		
def eventHandling():
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
		if event.type == MOUSEBUTTONDOWN:
			hit = duck.rect.collidepoint(aim.rect.centerx, aim.rect.centery)
			if hit == True:
				score.value += 1
			if hit == False:
				score.value -= 1
			if score.value < 0:
				score.value = 0 
			
initPyGame()
screen = pygame.display.set_mode((500, 375), 0, 32)
clock = pygame.time.Clock()
framesPerSecond = 20
score = scoreClass()
background = backgroundClass()
aim = aimClass()
duck = duckClass(70, 10)

allsprites = pygame.sprite.RenderPlain((aim, duck))


while True:
	## Game Loop
	clock.tick(framesPerSecond)
	eventHandling()
	background.draw()
	score.update()
	allsprites.update()
	allsprites.draw(screen)
	
	pygame.display.update()
