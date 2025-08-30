import pygame

pygame.init()

# Display Dimensions (will be changed to automatically detect screen size later)
displayHorizontal: int = 1920
displayVertical: int = 1080
display: pygame.display = pygame.display.set_mode((displayHorizontal, displayVertical))

gameActive: bool = True


while gameActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameActive = False
