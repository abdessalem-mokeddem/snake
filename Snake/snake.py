import pygame
import time
import random

snake_speed = 15
fenetre_x = 720
fenetre_y = 480
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Jeu du Snake')
jeu_ouvert = pygame.display.set_mode((fenetre_x, fenetre_y))


fps = pygame.time.Clock()


snake_position = [100, 50]

snake = [[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]

fruit_position = [random.randrange(1, (fenetre_x//10)) * 10,
				random.randrange(1, (fenetre_y//10)) * 10]

fruits_apparition = True


direction = 'Droite'
change = direction

score = 0


def show_score(choice, color, font, size):

	
	score = pygame.font.SysFont(font, size)
	
	
	score_surface = score.render('Score : ' + str(score), True, color)
	
	
	score_rect = score_surface.get_rect()
	
	
	jeu_ouvert.blit(score_surface, score_rect)


def game_over():

	mes_fonts = pygame.font.SysFont('Calibri', 50)
	
	
	fin_de_partie_surface = mes_fonts.render(
		'Ton score est de  : ' + str(score), True, red)
	
	
	fin_de_partie = fin_de_partie_surface.get_rect()
	

	fin_de_partie.midtop = (fenetre_x/2, fenetre_y/4)
	
	
	jeu_ouvert.blit(fin_de_partie_surface, fin_de_partie)
	pygame.display.flip()
	

	time.sleep(2)
	

	pygame.quit()

	quit()



while True:
	
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change = 'Monte'
			if event.key == pygame.K_DOWN:
				change = 'Bas'
			if event.key == pygame.K_LEFT:
				change = 'Gauche'
			if event.key == pygame.K_RIGHT:
				change = 'Droite'

	if change == 'Monte' and direction != 'Bas':
		direction = 'Monte'
	if change == 'Bas' and direction != 'Monte':
		direction = 'Bas'
	if change == 'Gauche' and direction != 'Droite':
		direction = 'Gauche'
	if change == 'Droite' and direction != 'Gauche':
		direction = 'Droite'

	
	if direction == 'Monte':
		snake_position[1] -= 10
	if direction == 'Bas':
		snake_position[1] += 10
	if direction == 'Gauche':
		snake_position[0] -= 10
	if direction == 'Droite':
		snake_position[0] += 10

	
	snake.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 10
		fruits_apparition = False
	else:
		snake.pop()
		
	if not fruits_apparition:
		fruit_position = [random.randrange(1, (fenetre_x//10)) * 10,
						random.randrange(1, (fenetre_y//10)) * 10]
		
	fruits_apparition = True
	jeu_ouvert.fill(black)
	
	for pos in snake:
		pygame.draw.rect(jeu_ouvert, green,
						pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(jeu_ouvert, white, pygame.Rect(
		fruit_position[0], fruit_position[1], 10, 10))

	if snake_position[0] < 0 or snake_position[0] > fenetre_x-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > fenetre_y-10:
		game_over()


	for block in snake[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	
	show_score(1, white, 'Arial', 20)

	pygame.display.update()

	fps.tick(snake_speed)
