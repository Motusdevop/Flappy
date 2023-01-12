import pygame
from random import randint, random
pygame.init()
pygame.mixer.init()

#create screen
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Flappy by Motus')
timer = pygame.time.Clock()

#game dict:
bg = pygame.transform.scale(pygame.image.load('bg.jpg'), (1000, 800))
bird = pygame.transform.scale(pygame.image.load('bird.png'), (100,80))
BLACK = (0, 0, 0)
GREEN = (30,89,69)
BLUE = (176,183,198)
wing = pygame.mixer.Sound('wing.wav')
point = pygame.mixer.Sound('point.wav')
die = pygame.mixer.Sound('die.wav')

#game varials:
play = True
score = 0
speed = 7
y_speed = 7
bird_x, bird_y = (100, 400)
FPS = 60
gravity = 0.3
trubs = [[[300, 0, 60, 400], [300, 600, 60 , 770]], [[800, -100, 60, 400], [800, 500, 60 , 770]]]
y_change = 0
gameover = False

def collision(trubs):
	global bird_x
	global bird_y
	global gameover
	for i in range(len(trubs)):
		trub = pygame.Rect(trubs[i][0][0], trubs[i][0][1], 60, 360)
		trub2 = pygame.Rect(trubs[i][1][0], trubs[i][1][1], 60, 360)
		if trub.collidepoint(bird_x + 90, bird_y) or trub2.collidepoint(bird_x + 90, bird_y + 50):
			die.play()
			gameover = True

def update_y(y_change, y_pos):
	global gravity
	y_change += gravity
	y_pos += y_change
	return y_change, y_pos

def update_change(y_change):
	y_change = - y_speed
	return y_change

def update_trubs(trubs):
	global speed
	global score
	if not gameover:
		for i in range(len(trubs)):
			if trubs[i][0][0] < -60:
				y = randint(-370, 0)
				trubs[i][0][1] = y
				trubs[i][1][1] = 600 + y

				trubs[i][0][0] += randint(1100, 1300)
				trubs[i][1][0] = trubs[i][0][0]
				point.play()
				score += 1
			else:
				trubs[i][0][0] -= speed
				trubs[i][1][0] -= speed
	return trubs

while play:
	timer.tick(FPS)

	y_change, bird_y = update_y(y_change, bird_y)
	trubs = update_trubs(trubs)

	screen.blit(bg, (0, 0))
	screen.blit(bird, (bird_x, bird_y))
	game_over_text = pygame.font.Font('Samson.ttf', 24).render(('SCORE: ' + str(score)), True, BLUE)
	screen.blit(game_over_text, (0, 0))

	collision(trubs)

	for i in range(len(trubs)):
		pygame.draw.rect(screen, GREEN, trubs[i][0], 0, 3)
		pygame.draw.rect(screen, GREEN, trubs[i][1], 0, 3)
		
	if gameover:
		FPS = 1
		game_over_text = pygame.font.Font('Samson.ttf', 60).render(('GAME OVER PRESS SPACEBAR'), True, BLUE)
		screen.blit(game_over_text, (170, 260))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not gameover:
			wing.play()
			y_change = update_change(y_change)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and gameover:
				gameover = False
				FPS = 60
				bird_y = 400
				trubs = [[[300, 0, 60, 400], [300, 600, 60 , 770]], [[800, -100, 60, 400], [800, 500, 60 , 770]]]
				y_change = 0
				score = 0

	if bird_y >= 800 or bird_y <= 0:
		die.play()
		gameover = True
	pygame.display.flip()

pygame.quit()