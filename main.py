import pygame

pygame.init()

#create screen
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Flappy by Motus')
timer = pygame.time.Clock()

#game dict:
bg = pygame.transform.scale(pygame.image.load('bg.jpg'), (1000, 800))
bird = pygame.transform.scale(pygame.image.load('bird.png'), (100,80))
BLACK = (0, 0, 0)

#game varials:
play = True
speed = 5
y_speed = 5
bird_x, bird_y = (100, 400)
FPS = 60
gravity = 0.2
trubs = [[350, 0, 20, 500]]
block = 0
y_change = 0

def update_y(y_change, y_pos):
	global gravity
	y_change += gravity
	y_pos += y_change
	return y_change, y_pos

def update_change(y_change):
	y_change = - y_speed
	return y_change
while play:
	y_change, bird_y = update_y(y_change, bird_y)
	blocks = []
	timer.tick(FPS)
	screen.blit(bg, (0, 0))
	screen.blit(bird, (100, bird_y))
	for i in range(len(trubs)):
		block = pygame.draw.rect(screen, BLACK, trubs[i], 0, 3)
		blocks.append(block)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			y_change = update_change(y_change)

	pygame.display.flip()

pygame.quit()