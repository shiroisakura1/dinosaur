import pygame
import random

pygame.init()
score = 0
font = pygame.font.Font(None, 36)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

cloud_speed = 2
cactus_speed = 2

WIDTH, HEIGHT = 600, 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur")

dino_image = pygame.image.load("dino.png")
cactus_image = pygame.image.load("cactus.png")
cloud_image = pygame.image.load("cloud.png")
game_over_image = pygame.image.load("game_over.png")

button_width = game_over_image.get_width()
button_height = game_over_image.get_height()

button_x = WIDTH // 2 - button_width // 2
button_y = HEIGHT // 2 - button_height // 2

button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

button_show = False

paused = False

def draw_button():
	global paused
	screen.blit(game_over_image, (button_x, button_y))
	paused = True

def press_button():
	global paused, button_show, score
	score = 0
	while len(cactus_list) != 0:
		cactus_list.pop(0)
	paused = False
	button_show = False
	create_cactus()

cloud_x = WIDTH
cloud_y = random.randint(0, 50)

dino_x = 20
dino_y = 150
velocity = 0
dino_jumping = False

cactus_list = []
next_cactus_time = 1

def jump():
	global dino_jumping, velocity
	if dino_jumping == False:
		velocity -= 3
		dino_jumping = True

def create_cactus():
	cactus_x = WIDTH
	cactus_Y = 150
	cactus_list.append([cactus_x, cactus_Y])

create_cactus()

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and paused == False:
				jump()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if button_rect.collidepoint(event.pos) and button_show:
				press_button()

	#cloud_move()
	cloud_x -= 0.8

	if paused == False:
		for i in range(len(cactus_list)):
			cactus_list[i][0] -= cactus_speed
			if cactus_list[i][0] + cactus_image.get_width() < 0:
				cactus_list.pop(i)
				break

	if cactus_list[-1][0] < 450:
		next_cactus_time -= 0.1
		if next_cactus_time <= 0:
			create_cactus()
			next_cactus_time = random.randint(1, 20)

	dino_y += velocity
	velocity += 0.08
	if dino_y >= 150:
		velocity = 0
		dino_y = 150
		dino_jumping = False

	# collision
	for cactus_x, cactus_y, in cactus_list:
		if dino_x + dino_image.get_width() > cactus_x and \
			dino_x < cactus_x + cactus_image.get_width() and \
			dino_y + dino_image.get_height() > cactus_y and \
			dino_y < cactus_y + cactus_image.get_height():
			button_show = True

	screen.fill(WHITE)
	screen.blit(cloud_image, (cloud_x, cloud_y))
	screen.blit(dino_image, (dino_x, dino_y))
	for cactus_x, cactus_y in cactus_list:
		screen.blit(cactus_image, (cactus_x, cactus_y))

	if button_show:
		draw_button()

	pygame.display.update()
	pygame.time.Clock().tick(FPS)











































































































































































