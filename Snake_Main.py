import pygame

import Snake_Display


def main():
    # Boolean to determine if the application is running
    gameOpen: bool = True
    # Boolean to determine if the game is running (as opposed to paused)
    gameActive: bool = False

    # Make the grid for the screen
    Snake_Display.makeGrid()

    # Main loop
    myGame = Snake_Display.pygame
    while gameOpen:
        for event in myGame.event.get():
            if event.type == myGame.QUIT:
                gameOpen = False
            
            # Using the "and" keyword to prevent an error when accessing a 'key' method of an event that does not have a 'key' method
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                gameActive = not gameActive
                print(gameActive)
            
        myGame.display.update()

# Uses a linked list of coordinates to represent the snake
class snakeNode:
    def __init__(self, coordinates: list[int, int]) -> None:
        self.coordinates = coordinates
        self.next = None
class snake:
    def __init__(self) -> None:
        self.head: snakeNode = snakeNode([0, 0])
    def growTail(self, coordinates: list[int, int]) -> None:
        tailNode: snakeNode = snakeNode(coordinates)
        currentNode: snakeNode = self.head
        while currentNode.next:
            currentNode: snakeNode = currentNode.next
        currentNode.next = tailNode

if __name__ == "__main__":
    main()