import pygame

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

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 28
HEIGHT = 28

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = [[0 for x in range(15)] for y in range(15)]    # Add an empty array that will hold each cell in this row

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [500, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Ludo")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(GRAY)

    # Draw the grid
    for row in range(15):
        for column in range(15):
            color = WHITE
            if (((row >= 0 and row < 6) or (row > 8 and row < 15)) and (column < 6 or column > 8)) \
                or (column == 7 and row > 7 and row < 14) \
                or (column == 7 and row > 0 and row < 7):
                color = BLACK
            if (row == 2 and column == 2) or (row == 3 and column == 3):
                color = DARK_RED
            if (row == 12 and column == 12) or (row == 11 and column == 11):
                color = DARK_GREEN
            elif (row == 7 and column > 7 and column < 14):
                color = GREEN
            elif (row == 7 and column < 7 and column > 0):
                color = RED
            elif ((row == 8) and (column == 13 or column == 2)) or ((row == 6) and (column == 12 or column == 1)) \
                  or ((column == 6) and (row == 13 or row == 2)) or ((column == 8) and (row == 12 or row == 1)):
                color = PURPLE
            elif (row > 5 and row < 9 and column > 5 and column < 9):
                color = GOLDEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
