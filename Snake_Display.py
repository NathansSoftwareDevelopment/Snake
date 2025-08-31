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
    setattr(pygame, 'grid', {})
    boxHorizontal: int = displayHorizontal / gridHorizontal
    boxVertical: int = displayVertical / gridVertical
    for x in range(0, gridHorizontal):
        pygame.grid[x] = {}
        for y in range (0, gridVertical):
            box: pygame.Rect = pygame.Rect(x*boxHorizontal, y*boxVertical, boxHorizontal, boxVertical)
            pygame.grid[x][y] = box
            pygame.draw.rect(display, whiteRGB, box, 1)

# Display the Snake
greenRGB: tuple = (0, 255, 0)
def displaySnakeNode(snakeNode) -> None:
    xCoordinate = snakeNode.coordinates[0]
    yCoordinate = snakeNode.coordinates[1]
    pygame.draw.rect(display, greenRGB, pygame.grid[xCoordinate][yCoordinate], 1000)