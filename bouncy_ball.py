import random, time, pygame, sys
from pygame.locals import *

FPS = 25
size = (1024, 720)
speed = [5, 5]

BLACK = (0, 0, 0)

paddle = pygame.image.load('paddle.png')
paddleRect = paddle.get_rect(center = (512, 680))
ball = pygame.image.load('ball.png')
ballRect = ball.get_rect(center = (512, 360))

BGCOLOR = BLACK

def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT
	pygame.init()
	pygame.mouse.set_visible(0)
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode(size)
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('bouncy ball')
 
	while True:
		runGame()

def runGame():
	while True:
		mousex, mousey = pygame.mouse.get_pos()
		mousey = 680
		chekingForQuit()
		DISPLAYSURF.fill(BGCOLOR)

		ballMovement()

		DISPLAYSURF.blit(paddle, (mousex, mousey))
		DISPLAYSURF.blit(ball, ballRect)
		pygame.display.update()

		FPSCLOCK.tick(FPS)


def terminate():
	pygame.quit()
	sys.exit()

def chekingForQuit():
	for event in pygame.event.get(QUIT):
		terminate()

def ballMovement():
	global ballRect
	global paddleRect
	mousex, mousey = pygame.mouse.get_pos()
	mousey = 680
	ballRect = ballRect.move(speed)
	if ballRect.left < 0 or ballRect.right > size[0]:
		speed[0] = - speed[0]
	if ballRect.top < 0 or ballRect.bottom > size[1]:
		speed[1] = - speed[1]
	

if __name__ == '__main__':
	main()