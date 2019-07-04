from modules.Board import Board
from modules.Player import Player
from modules.Piece import Piece
import random
import pygame


class Ludo:

    # This sets the self.WIDTH and self.HEIGHT of each grid location
    WIDTH = 28
    HEIGHT = 28

    # This sets the margin between each cell
    MARGIN = 5

    # Initial value of dice as default
    dice = 0

    def __init__(self):

        piece_a1 = Piece(1)
        piece_a2 = Piece(2)
        pieces_a = [piece_a1, piece_a2]

        piece_b1 = Piece(1)
        piece_b2 = Piece(2)
        pieces_b = [piece_b1, piece_b2]

        # attributes
        self.playerA = Player("GREEN", pieces_a, 'A')
        self.playerB = Player("RED", pieces_b, 'B')
        self.board = Board()

    def render(self):

        green1_route = self.playerA.get_route(1)
        green2_route = self.playerA.get_route(2)
        red1_route = self.playerB.get_route(1)
        red2_route = self.playerB.get_route(2)

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        grid = [[0 for x in range(15)] for y in range(15)]    # Add an empty array that will hold each cell in this row

        # Set row 1, cell 5 to one. (Remember rows and
        # column numbers start at zero.)
        grid[1][5] = 1

        # Loop until the user clicks the close button.
        done = False

        self.board.draw(2, 2, 3, 3, 12, 12, 11, 11, 0)     # initial state of board

        # coordinates = []
        player_turn = 0
        lock = 0

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (self.WIDTH + self.MARGIN)
                    row = pos[1] // (self.HEIGHT + self.MARGIN)
                    pos = (row, column)
                    print(pos)
                    a = green1_route[self.playerA.pieces[0].current_pos]
                    b = green2_route[self.playerA.pieces[1].current_pos]
                    c = red1_route[self.playerB.pieces[0].current_pos]
                    d = red2_route[self.playerB.pieces[1].current_pos]
                    print(red1_route[self.playerB.pieces[0].current_pos])

                    if a == pos or b == pos or c == pos or d == pos and lock == 1:
                        if a == pos and player_turn == 0:
                            if self.playerA.pieces[0].state != 'home':
                                self.playerA.pieces[0].current_pos += self.dice
                                piece = self.playerA.pieces[0]
                                new_position = green1_route[piece.current_pos]
                                self.board.draw(c[0], c[1], d[0], d[1], new_position[0], new_position[1], b[0], b[1],
                                                self.dice)
                            elif self.dice == 6:
                                if a == (12, 12):
                                    self.playerA.pieces[0].current_pos += 1
                                else:
                                    self.playerA.pieces[0].current_pos += self.dice + 1
                                piece = self.playerA.pieces[0]
                                new_position = green1_route[piece.current_pos]
                                self.playerA.pieces[0].state = 'safe'
                                self.board.draw(c[0], c[1], d[0], d[1], new_position[0], new_position[1], b[0], b[1],
                                                self.dice)
                            player_turn = 1  # keep alternating player turns

                        elif b == pos and player_turn == 0:
                            if self.playerA.pieces[1].state != 'home':
                                self.playerA.pieces[1].current_pos += self.dice
                                piece = self.playerA.pieces[1]
                                new_position = green2_route[piece.current_pos]
                                self.board.draw(c[0], c[1], d[0], d[1], a[0], a[1], new_position[0], new_position[1],
                                                self.dice)
                            elif self.dice == 6:
                                if b == (11, 11):
                                    self.playerA.pieces[1].current_pos += 1
                                else:
                                    self.playerA.pieces[1].current_pos += self.dice + 1
                                piece = self.playerA.pieces[1]
                                new_position = green2_route[piece.current_pos]
                                self.playerA.pieces[1].state = 'safe'
                                self.board.draw(c[0], c[1], d[0], d[1], a[0], a[1], new_position[0], new_position[1],
                                                self.dice)
                            player_turn = 1  # keep alternating player turns

                        elif c == pos and player_turn == 1:
                            if self.playerB.pieces[0].state != 'home':
                                self.playerB.pieces[0].current_pos += self.dice
                                piece = self.playerB.pieces[0]
                                new_position = red1_route[piece.current_pos]
                                self.board.draw(new_position[0], new_position[1], d[0], d[1], a[0], a[1], b[0], b[1],
                                                self.dice)
                            elif self.dice == 6:
                                if c == (2, 2):
                                    self.playerB.pieces[0].current_pos += 1
                                else:
                                    self.playerB.pieces[0].current_pos += self.dice + 1
                                piece = self.playerB.pieces[0]
                                new_position = red1_route[piece.current_pos]
                                self.playerB.pieces[0].state = 'safe'
                                self.board.draw(new_position[0], new_position[1], d[0], d[1], a[0], a[1], b[0], b[1],
                                                self.dice)
                            player_turn = 0  # keep alternating player turns

                        elif d == pos and player_turn == 1:
                            if self.playerB.pieces[1].state != 'home':
                                self.playerB.pieces[1].current_pos += self.dice
                                piece = self.playerB.pieces[1]
                                new_position = red2_route[piece.current_pos]
                                self.board.draw(c[0], c[1], new_position[0], new_position[1], a[0], a[1], b[0], b[1],
                                                self.dice)
                            elif self.dice == 6:
                                if d == (3, 3):
                                    self.playerB.pieces[1].current_pos += 1
                                else:
                                    self.playerB.pieces[1].current_pos += self.dice + 1
                                piece = self.playerB.pieces[1]
                                new_position = red2_route[piece.current_pos]
                                self.playerB.pieces[1].state = 'safe'
                                self.board.draw(c[0], c[1], new_position[0], new_position[1], a[0], a[1], b[0], b[1],
                                                self.dice)

                            player_turn = 0  # keep alternating player turns

                        lock = 0   # the player can roll the dice now
                        self.dice = 0

                    # coordinates.append(pos)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # User presses enter
                    if lock == 0:
                        self.dice = random.randint(5, 6)
                        self.board.draw(red1_route[self.playerB.pieces[0].current_pos][0]
                                        , red1_route[self.playerB.pieces[0].current_pos][1]
                                        , red2_route[self.playerB.pieces[1].current_pos][0]
                                        , red2_route[self.playerB.pieces[1].current_pos][1]
                                        , green1_route[self.playerA.pieces[0].current_pos][0]
                                        , green1_route[self.playerA.pieces[0].current_pos][1]
                                        , green2_route[self.playerA.pieces[1].current_pos][0]
                                        , green2_route[self.playerA.pieces[1].current_pos][1]
                                        , self.dice)
                        lock = 1

                # with open('data/PlayerB_route.pkl', 'wb') as f:
                #     pickle.dump(coordinates, f)

    def main(self):
        self.render()
