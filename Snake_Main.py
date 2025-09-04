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
    mySnake: snake = snake()
    clock = myGame.time.Clock()
    framesPerSecond: int = 4
    movementDirection: pygame.key = pygame.K_d

    appleCoordinates: list[int] = [7, 4]
    Snake_Display.displaySnake(mySnake)

    while gameOpen:
        for event in myGame.event.get():
            if event.type == myGame.QUIT:
                gameOpen = False
            
            # If the event isn't a keystroke then ignore it
            elif event.type != pygame.KEYDOWN:
                pass
            
            elif event.key == pygame.K_ESCAPE:
                gameActive = not gameActive
                print(gameActive)
            elif event.type == pygame.KEYDOWN:
                movementDirection = event.key

        clock.tick(framesPerSecond)
        mySnake.move(movementDirection)

        Snake_Display.displaySnake(mySnake)
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
    
    def move(self, direction: pygame.key) -> None:
        originalCoordinates: list[int, int] = self.head.coordinates.copy()

        northSouthIndex: int = 1
        eastWestIndex: int = 0
        southEastChange: int = 1
        northWestChange: int = -1
        match direction:
            case pygame.K_w:
                self.head.coordinates[northSouthIndex] += northWestChange
            case pygame.K_a:
                self.head.coordinates[eastWestIndex] += northWestChange
            case pygame.K_s:
                self.head.coordinates[northSouthIndex] += southEastChange
            case pygame.K_d:
                self.head.coordinates[eastWestIndex] += southEastChange
            case _:
                return
        Snake_Display.clearPixel(originalCoordinates[0], originalCoordinates[1])
        
        if self.head.next:
            self.moveTail(originalCoordinates)
    def moveTail(self, headCoordinates: list[int, int]) -> None:
        # Move each node to the previous position of the node ahead of it
        oldPartCoordinates = headCoordinates.copy()
        currentNode: snakeNode = self.head.next
        while currentNode:
            currentPartCoordinates: list[int, int] = currentNode.coordinates
            currentNode.coordinates = oldPartCoordinates
            oldPartCoordinates = currentPartCoordinates
            
            currentNode = currentNode.next
        Snake_Display.clearPixel(oldPartCoordinates[0], oldPartCoordinates[1])
        

if __name__ == "__main__":
    main()