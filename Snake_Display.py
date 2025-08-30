import pygame

pygame.init()
display = pygame.display.set_mode((1920, 1080))

gameActive = True

while gameActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False