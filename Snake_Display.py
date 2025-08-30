import pygame

pygame.init()

# Display Dimensions (will be changed to automatically detect screen size later)
displayHorizontal = 1920
displayVertical = 1080
display = pygame.display.set_mode((displayHorizontal, displayVertical))

gameActive = True

while gameActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False