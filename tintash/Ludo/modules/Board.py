import pygame
import random


class Board:

    # Define some colors
    BLACK = (50, 50, 50)
    GRAY = (60, 60, 60)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 150, 0)
    RED = (255, 0, 0)
    DARK_RED = (150, 0, 0)
    PURPLE = (128, 0, 128)
    GOLDEN = (197, 179, 88)

    # This sets the self.WIDTH and self.HEIGHT of each grid location
    WIDTH = 28
    HEIGHT = 28

    # This sets the margin between each cell
    MARGIN = 5

    # This sets the size of the window
    WINDOW_SIZE = [500, 500]

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        # Set title of screen
        pygame.display.set_caption("Ludo")

        # Set the screen background
        self.screen.fill(self.GRAY)

    def draw(self, rowA1, columnA1, rowA2, columnA2, rowB1, columnB1, rowB2, columnB2, dice):
        # Draw the grid
        for row in range(15):
            for column in range(15):
                color = self.WHITE
                if (((row >= 0 and row < 6) or (row > 8 and row < 15)) and (column < 6 or column > 8)) \
                        or (column == 7 and row > 7 and row < 14) \
                        or (column == 7 and row > 0 and row < 7):
                    color = self.BLACK
                elif ((row == 8) and (column == 13 or column == 2)) or ((row == 6) and (column == 12 or column == 1)) \
                        or ((column == 6) and (row == 13 or row == 2)) or ((column == 8) and (row == 12 or row == 1)):
                    color = self.PURPLE
                if (row == rowA1 and column == columnA1) or (row == rowA2 and column == columnA2):
                    color = self.DARK_RED
                if (row == rowB1 and column == columnB1) or (row == rowB2 and column == columnB2):
                    color = self.DARK_GREEN
                elif (row == 7 and column > 7 and column < 14):
                    color = self.GREEN
                elif (row == 7 and column < 7 and column > 0):
                    color = self.RED
                elif (row > 5 and row < 9 and column > 5 and column < 9):
                    color = self.GOLDEN

                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                  self.WIDTH,
                                  self.HEIGHT])
                color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
                text = str(dice)
                font = pygame.font.Font(None, 50)
                text = font.render(text, True, color)
                self.screen.blit(text, (240, 235))  # dice number

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # with open('PlayerB_route.pkl', 'wb') as f:    # For saving the coordinates in a file as I click on the tiles
        #     pickle.dump(coordinates, f)

        # # Be IDLE friendly. If you forget this line, the program will 'hang'
        # # on exit.
        # pygame.quit()








