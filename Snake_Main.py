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
        myGame.display.update()
    

if __name__ == "__main__":
    main()