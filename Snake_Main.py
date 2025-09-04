import random

import pygame

import Snake_Display


def main():
    # Boolean to determine if the application is running
    gameOpen: bool = True
    # Boolean to determine if the game is running (as opposed to paused)
    gamePaused: bool = False

    # Make the grid for the screen
    Snake_Display.makeGrid()

    # Main loop
    myGame = Snake_Display.pygame
    mySnake: snake = snake()
    clock = myGame.time.Clock()
    framesPerSecond: int = 4
    movementDirection: pygame.key = pygame.K_d

    appleCoordinates: list[int] = spawnApple(mySnake)
    Snake_Display.displayApple(appleCoordinates)
    Snake_Display.displaySnake(mySnake)
    myGame.display.update()

    while gameOpen:
        for event in myGame.event.get():
            if event.type == myGame.QUIT:
                gameOpen = False
            
            # If the event isn't a keystroke then ignore it
            elif event.type != pygame.KEYDOWN:
                pass
            
            elif event.key == pygame.K_ESCAPE:
                gamePaused = not gamePaused
                print(gamePaused)
            elif gamePaused: # If the game is paused don't register other keystrokes
                break

            elif event.type == pygame.KEYDOWN:
                movementDirection = event.key

        if gamePaused: # If the game is paused don't do anything
            continue

        oldCoordinates: list[int] = mySnake.getEndCoordinates()
        mySnake.move(movementDirection)
        if mySnake.head.coordinates == appleCoordinates:
            mySnake.growTail(oldCoordinates)
            appleCoordinates = spawnApple(mySnake)
            Snake_Display.displayApple(appleCoordinates)

        Snake_Display.displaySnake(mySnake)

        clock.tick(framesPerSecond)
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
    def getEndCoordinates(self) -> list[int]:
        currentNode: snakeNode = self.head
        coordinates: list[int]
        while currentNode:
            coordinates = currentNode.coordinates.copy()
            currentNode = currentNode.next
        return coordinates

# Make a list for every valid coordinate, remove each of the snake's node's locations from the list, pick an empty coordinate
def spawnApple(inputSnake: snake) -> list[int]:
    coordinateList = [[x, y] for x in range(Snake_Display.gridHorizontal) for y in range(Snake_Display.gridVertical)]
    currentNode = inputSnake.head
    while currentNode:
        coordinateList.remove(currentNode.coordinates)
        currentNode = currentNode.next
    return random.choice(coordinateList)
        
        

if __name__ == "__main__":
    main()