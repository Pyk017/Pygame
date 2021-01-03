import pygame
pygame.init()

screen_WIDTH = 500
screen_HEIGHT = 480

screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))

pygame.display.set_caption("Jump Game")


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1, 0.0)

score = 0

class Player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.velocity = 5
		self.jumpCount = 10
		self.isJump = False
		self.left = False
		self.right = False
		self.walkCount = 0
		self.standing = True
		self.hitbox = (self.x + 17, self.y + 11, 29, 52)

	def draw(self, screen):
		if self.walkCount + 1 >= 27:
			self.walkCount = 0

		if not(self.standing):
			if self.left:
				screen.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
				self.walkCount += 1
			elif self.right:
				screen.blit(walkRight[self.walkCount // 3], (self.x, self.y))
				self.walkCount += 1
		else:
			if self.right:
				screen.blit(walkRight[0], (self.x, self.y))
			else:
				screen.blit(walkLeft[0], (self.x, self.y))
		self.hitbox = (self.x + 17, self.y + 11, 29, 52)
		# pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

	def hit(self):
		self.x = 60
		self.y = 410
		self.jumpCount = 10
		self.isJump = False
		self.walkCount = 0
		font1 = pygame.font.SysFont('comicsans', 100)
		text = font1.render('-5', 1, (255, 0, 0))
		screen.blit(text, (250 - (text.get_width()/2), 200))
		pygame.display.update()
		i = 0
		while i < 300:
			pygame.time.delay(10)
			i += 1
			for event in  pygame.event.get():
				if event.type == pygame.QUIT:
					i = 301
					pygame.quit()


class Projectile(object):
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.velocity = 8 * facing

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


class Enemy(object):
	walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
	walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

	def __init__(self, x, y, width, height, end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x, self.end]
		self.walkCount = 0
		self.velocity = 3
		self.hitbox = (self.x + 17, self.y + 2, 31, 57)
		self.health = 10
		self.visible = True

	def draw(self, screen):
		self.move()
		if self.visible:
			if self.walkCount + 1 >= 33:
				self.walkCount =  0

			if self.velocity > 0:
				screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
				self.walkCount += 1

			else:
				screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
				self.walkCount += 1
			self.hitbox = (self.x + 17, self.y + 2, 31, 57)
			pygame.draw.rect(screen, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
			pygame.draw.rect(screen, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
			# pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


	def move(self):
		if self.velocity > 0:
			if self.x + self.velocity < self.path[1]:
				self.x += self.velocity
			else:
				self.velocity *= -1
				self.walkCount = 0

		else:
			if self.x - self.velocity > self.path[0]:
				self.x += self.velocity
			else:
				self.velocity *= -1
				self.walkCount = 0


	def hit(self):
		if self.health > 0:
			self.health -= 1
		else:
			self.visible = False
		print("HIT!!")




def redrawGameWindow(man, bullets):
	screen.blit(bg, (0, 0))
	text = font.render('Score: ' + str(score), 1, (0, 0, 0))
	screen.blit(text, (350, 10))
	man.draw(screen)
	goblin.draw(screen)
	for bullet in bullets:
		bullet.draw(screen)

	pygame.display.update()





font = pygame.font.SysFont('comicsnas', 30, True)
man = Player(50, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
bulletloop = 0
bullets = []

# mainloop
running = True
while running:
	clock.tick(27)
	pygame.time.delay(27)

	if goblin.visible:
		if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
			if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0]  < goblin.hitbox[0] + goblin.hitbox[2]:
				man.hit()
				score -= 5


	if bulletloop > 0:
		bulletloop += 1
	if bulletloop > 3:
		bulletloop = 0


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	for bullet in bullets:
		if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
			if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius  < goblin.hitbox[0] + goblin.hitbox[2]:
				goblin.hit()
				hitSound.play()
				score += 1
				bullets.pop(bullets.index(bullet))

		if bullet.x < 500 and bullet.x > 0:
			bullet.x += bullet.velocity
		else:
			bullets.pop(bullets.index(bullet))


	keys = pygame.key.get_pressed()

	if keys[pygame.K_SPACE] and bulletloop == 0:
		bulletSound.play()
		facing = -1 if man.left else 1

		if len(bullets) < 5:
			bullets.append(Projectile(man.x + (man.width//2), man.y + (man.height//2), 6, (0, 0, 0), facing))

		bulletloop = 1

	if keys[pygame.K_LEFT] and man.x > man.velocity:
		man.x -= man.velocity
		man.left = True
		man.right = False
		man.standing = False

	elif keys[pygame.K_RIGHT] and man.x < screen_WIDTH - man.width - man.velocity:
		man.x += man.velocity
		man.left = False
		man.right = True
		man.standing = False

	else:
		man.standing = True
		man.walkCount = 0


	if not(man.isJump):
		if keys[pygame.K_UP]:
			man.isJump = True
			man.right = False
			man.left = False
			man.walkCount = 0

	else:
		if man.jumpCount >= -10:
			neg = 1
			if man.jumpCount < 0:
				neg = -1
			man.y -= (man.jumpCount ** 2) * 0.5 * neg
			man.jumpCount -= 1

		else:
			man.isJump = False
			man.jumpCount = 10

	redrawGameWindow(man, bullets)

	


pygame.quit()

