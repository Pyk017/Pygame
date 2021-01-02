import pygame
pygame.init()

screen_WIDTH = 800
screen_HEIGHT = 600

screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))

pygame.display.set_caption("Jump Game")

x, y = 10, 580
width, height = 40, 50
velocity = 5

isJump = False
jumpCount = 10

running = True
while running:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x > velocity:
		x -= velocity

	if keys[pygame.K_RIGHT] and x < screen_WIDTH - width - velocity:
		x += velocity

	if not(isJump):
		if keys[pygame.K_UP] and y > velocity:
			y -= velocity

		if keys[pygame.K_DOWN] and y < screen_HEIGHT - height - velocity:
			y += velocity

		if keys[pygame.K_SPACE]:
			isJump = True

	else:
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1

		else:
			isJump = False
			jumpCount = 10



	screen.fill((0, 0, 0))
	pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
	pygame.display.update()


pygame.quit()

