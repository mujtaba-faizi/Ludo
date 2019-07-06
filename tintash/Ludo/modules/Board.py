import pygame
import random


class Board:

    # Define some colors
    BLACK = (0, 0, 0)
    GRAY = (60, 60, 60)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 150, 0)
    RED = (255, 0, 0)
    DARK_RED = (150, 0, 0)
    PURPLE = (128, 0, 128)
    GOLDEN = (197, 179, 88)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)

    # This sets the self.WIDTH and self.HEIGHT of each grid location
    WIDTH = 32
    HEIGHT = 32

    # This sets the margin between each cell
    MARGIN = 1

    # This sets the size of the window
    WINDOW_SIZE = [496, 497]

    color = BLACK

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        # Set title of screen
        pygame.display.set_caption("Ludo")

        # Set the screen background
        self.screen.fill(self.BLACK)

    def draw(self, row_a1, column_a1, row_a2, column_a2, row_b1, column_b1, row_b2, column_b2, dice, lock, player_turn):
        # Draw the grid
        for row in range(15):
            for column in range(15):
                color = self.WHITE
                if (0 <= row < 6 or 8 < row < 15) and (column < 6 or column > 8):
                    color = self.BLACK
                elif ((row == 8) and (column == 13 or column == 2)) or ((row == 6) and (column == 12 or column == 1)) \
                        or ((column == 6) and (row == 13 or row == 2)) or ((column == 8) and (row == 12 or row == 1)):
                    color = self.PURPLE
                if (row == row_a1 and column == column_a1) or (row == row_a2 and column == column_a2):
                    color = self.DARK_RED
                if (row == row_b1 and column == column_b1) or (row == row_b2 and column == column_b2):
                    color = self.DARK_GREEN
                elif row == 7 and 7 < column < 14:
                    color = self.GREEN
                elif row == 7 and 0 < column < 7:
                    color = self.RED
                elif 5 < row < 9 and 5 < column < 9:
                    color = self.GOLDEN
                if column == 7 and 7 < row < 14:
                    color = self.BLUE
                if column == 7 and 0 < row < 7:
                    color = self.YELLOW
                if row == 0 and column == 14:
                    if lock == 1:
                        color = self.WHITE
                    elif player_turn == 'green':
                        color = self.GREEN
                    elif player_turn == 'red':
                        color = self.RED

                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                  self.WIDTH,
                                  self.HEIGHT])

                if lock == 0:   # dice roll means new text
                    self.color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))

                font = pygame.font.Font(None, 50)
                text = str(dice)
                text = font.render(text, True, self.color)
                self.screen.blit(text, (238, 233))  # dice number

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # # Be IDLE friendly. If you forget this line, the program will 'hang'
        # # on exit.
        # pygame.quit()
