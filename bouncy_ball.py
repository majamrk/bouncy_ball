import random, time, pygame, sys
from pygame.locals import *

FPS = 25
BOARDWIDTH = 20
BOARDHEIGHT = 15

BLACK = (0, 0, 0)

BGCOLOR = BLACK



def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('Bouncy ball')

#	showTextScreen('Bouncy ball')
	while True:
		runGame()

def runGame():
	while True:
		chekingForQuit()
		DISPLAYSURF.fill(BGCOLOR)

		pygame.display.update()
		FPSCLOCK.tick(FPS)

def terminate():
	pygame.quit()
	sys.exit()

def chekingForQuit():
	for event in pygame.event.get(QUIT):
		terminate()

if __name__ == '__main__':
	main()
