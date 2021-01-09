import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Yush Game')

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_red = (200, 0, 0)
bright_green = (0, 128, 0)

car_img = pygame.image.load("Car.png")
car_width = 79

game_icon = pygame.image.load("Car.png")
pygame.display.set_icon(game_icon)

pause = False


def blocks(block_x, block_y, block_w, block_h, color):
    pygame.draw.rect(game_display, color, [block_x, block_y, block_w, block_h])


def car(x, y):
    game_display.blit(car_img, (x, y))


# car_speed = 0
def blocks_score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Score : ' + str(count), True, black)
    game_display.blit(text, (0, 0))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font("freesansbold.ttf", 100)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = (int(display_width/2), int(display_height/2))
    game_display.blit(text_surf, text_rect)

    pygame.display.update()
    time.sleep(2)
    game_loop()


def unpause():
    global pause
    pause = False


def paused():
    large_text = pygame.font.SysFont("comicsansms", 100)
    text_surf, text_rect = text_objects("Paused", large_text)
    text_rect.center = (int(display_width // 2), 150)
    game_display.blit(text_surf, text_rect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 300, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 300, 100, 50, red, bright_red, game_quit)

        pygame.display.update()
        clock.tick(15)


def button(message, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(game_display, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(game_display, inactive_color, (x, y, width, height))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(message, small_text)
    text_rect.center = ((x + (width // 2)), (y + (height // 2)))
    game_display.blit(text_surf, text_rect)


def game_into(text):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)
        large_text = pygame.font.SysFont("comicsansms", 50)
        text_surf, text_rect = text_objects(text, large_text)
        text_rect.center = (int(display_width / 2), 150)
        game_display.blit(text_surf, text_rect)

        button("Start!", 150, 300, 100, 50, green, bright_green, game_loop)
        button("Exit!", 550, 300, 100, 50, red, bright_red, game_quit)

        pygame.display.update()
        clock.tick(20)


def game_quit():
    pygame.quit()
    quit()


def crash():
    # message_display('You Crashed!')
    large_text = pygame.font.SysFont('comicsansms', 100)
    text_surf, text_rect = text_objects('You Crashed!', large_text)
    text_rect.center = ((display_width//2), 150)
    game_display.blit(text_surf, text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 300, 150, 50, green, bright_green, game_loop)
        button("Quit", 550, 300, 150, 50, red, bright_red, game_quit)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    x = int(800 * 0.45)
    y = int(600 * 0.65)
    crashed = False
    x_change = 0
    score = 0

    block_start_x = random.randrange(0, display_width)
    block_start_y = -600
    block_speed = 7
    block_width = 100
    block_height = 100

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_SPACE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            # print(event)

        x += x_change
        game_display.fill(white)

        blocks(block_start_x, block_start_y, block_width, block_height, black)
        block_start_y += block_speed
        car(x, y)
        blocks_score(score)

        if x > display_width - car_width or x < 0:
            crash()

        if block_start_y > display_height:
            block_start_y = 0 - block_height
            block_start_x = random.randrange(0, display_width)
            score += 1
            block_speed += 1
            block_width += int(score * 1.2)

        if block_start_y > display_height:
            block_start_y = 0 - block_height
            block_start_x = random.randrange(0, display_width)

        if y < block_start_y + block_height:
            print('Y Crossover')

            if block_start_x < x < block_start_x + block_width or block_start_x < x + car_width < block_start_x \
                    + block_width:
                print('X Crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_into("Dodge if you can - By Y.K.")
game_loop()
pygame.quit()
quit()
