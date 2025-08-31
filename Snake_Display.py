import pygame

pygame.init()

# Display Dimensions (will be changed to automatically detect screen size later)
displayHorizontal: int = 1920
displayVertical: int = 1080
display: pygame.display = pygame.display.set_mode((displayHorizontal, displayVertical))

gameActive: bool = True

# Make a grid on the display with a number of boxes determined by the gridHorizontal and gridVertical variables
whiteRGB: tuple = (255, 255, 255)
gridHorizontal: int = 16
gridVertical: int = 9
def makeGrid() -> None:
    boxHorizontal: int = displayHorizontal / gridHorizontal
    boxVertical: int = displayVertical / gridVertical
    for x in range(0, gridHorizontal):
        for y in range (0, gridVertical):
            box: pygame.Rect = pygame.Rect(x*boxHorizontal, y*boxVertical, boxHorizontal, boxVertical)
            pygame.draw.rect(display, whiteRGB, box, 1)