import pygame
import winsound


class Ball:
    def __init__(self, x, y, width, height, dx, dy):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.dx = dx
        self.dy = dy


class Blocks:

    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed


def print_text(message):
    pygame.font.init()
    font = pygame.font.Font("OpenSans-Light.ttf", 24)
    textsurface = font.render(message, True, (150, 150, 150))
    win.blit(textsurface, (80, 25))


pygame.init()
win_h = 500
win = pygame.display.set_mode((win_h, win_h))

pygame.display.set_caption("Call of Python")

# ToDo:definition of elements
blockA = Blocks(15, 200, 15, 80, 6)
blockB = Blocks(470, 200, 15, 80, 6)
ball = Ball(200, 270, 20, 20, 5, 5)
score_a = 0
score_b = 0

# ToDo:main loop
run = True
while run:
    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # ToDo:keys event listener
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and blockA.y > 5:
        blockA.y -= blockA.speed
    if keys[pygame.K_s] and blockA.y < win_h - blockA.height + 5:
        blockA.y += blockA.speed
    if keys[pygame.K_UP] and blockB.y > 5:
        blockB.y -= blockB.speed
    if keys[pygame.K_DOWN] and blockB.y < win_h - blockB.height + 5:
        blockB.y += blockB.speed
    # ToDo:ball movement
    ball.x += ball.dx
    ball.y += ball.dy
    # ToDo:border checking
    if ball.y > win_h - ball.height:
        winsound.PlaySound("exporto.wav", winsound.SND_ASYNC)
        ball.y = win_h - ball.height
        ball.dy *= -1
    if ball.y < 0:
        winsound.PlaySound("exporto.wav", winsound.SND_ASYNC)
        ball.y = 0
        ball.dy *= -1
    if ball.x > win_h - ball.width:
        ball.x = 200
        ball.y = 270
        ball.dx *= -1
        score_a += 1
    if ball.x < 0:
        ball.x = 200
        ball.y = 270
        ball.dx *= -1
        score_b += 1
    # ToDo:block and ball collision
    if blockA.x + blockA.width > ball.x > blockA.x + blockA.width / 2 and ball.y < blockA.y + blockA.height and ball.y + ball.height > blockA.y:
        winsound.PlaySound("export.wav", winsound.SND_ASYNC)
        ball.x = blockA.x + blockA.width
        ball.dx *= -1
    if ball.x + ball.width > blockB.x and ball.x < blockB.x + blockB.width / 2 and ball.y < blockB.y + blockB.height and ball.y + ball.height > blockB.y:
        winsound.PlaySound("export.wav", winsound.SND_ASYNC)
        ball.x = blockB.x - ball.height
        ball.dx *= -1
    win.fill((0, 0, 0))
    # ToDo: printing text
    print_text("Player A: {}                     Player B: {}".format(score_a, score_b))
    # ToDo:drawing
    pygame.draw.rect(win, (0, 0, 225), (blockA.x, blockA.y, blockA.width, blockA.height))
    pygame.draw.rect(win, (0, 0, 225), (blockB.x, blockB.y, blockB.width, blockB.height))
    pygame.draw.rect(win, (90, 40, 50), (ball.x, ball.y, ball.width, ball.height))
    pygame.display.update()

pygame.quit()
