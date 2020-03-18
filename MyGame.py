import pygame
import random
import math
from threading import Timer
from Comet import Comet
from CometSpawner import CometSpawner

pygame.init()

# Load images
simonImg = pygame.image.load('simon.png')
leenaImg = pygame.image.load('leena.png')
koekkenImg = pygame.image.load('koekken.png')


# Game settings
width = 800
height = 378
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Leena kom herover")
# For lose text
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Simon spiste dig.. Tryk enter for at ghoste', True, (0, 0, 0), (255, 0, 0))
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)

# Player settings
x = width // 2
y = height // 2
radius = 8
vel = 3
# Score stuff
score = 0
scoreText = font.render(str(score), True, (0, 0, 0), (255, 255, 255))
scoreTextRect = scoreText.get_rect()
scoreTextRect.center = (width - 95, height - 20)


# Comet settings
spawner = CometSpawner(width, height)
comets = [Comet(5, 100, 200)]

# Functions


def spawn_comet_at_random():
    if random.randint(1, 50) == 1:
        comets.append(spawner.spawn_a_comet())


def draw_comet(comet):
    win.blit(simonImg, (comet.x, comet.y))


# Game loop
run = True
collided = False
while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x + radius < width - vel:
        x += vel
    if keys[pygame.K_UP] and y - radius > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y + radius < height - vel:
        y +=  vel
    if keys[pygame.K_RETURN] and collided:
        comets = []
        collided = False
        x = width // 2
        y = height // 2
        score = 0

    # Draw background
    win.blit(koekkenImg, (0, 0))

    # Draw the comets
    for comet in comets:
        comet.updateCoordinates(width, height)
        draw_comet(comet)

    # Check for any collision
    for comet in comets:
        dx = comet.x - x
        dy = comet.y - y
        if math.sqrt(dx * dx + dy * dy) < comet.size + radius:
            collided = True

    # Spawn a comet (randomly)
    spawn_comet_at_random()

    # Draw player and update score
    if not collided:
        win.blit(leenaImg, (x, y))
        score += 10

    # Text when lost
    if collided:
        win.blit(text, textRect)

    # Draw score
    scoreText = font.render(str(score), True, (0, 0, 0), (255, 255, 255))
    scoreText = font.render(str(score), True, (0, 0, 0), (255, 255, 255))
    win.blit(scoreText, scoreTextRect)

    pygame.display.update()

pygame.quit()