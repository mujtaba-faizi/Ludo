from modules.Board import Board
from modules.Player import Player
from modules.Piece import Piece
import random
import pygame
import pickle


class Ludo:

    # This sets the self.WIDTH and self.HEIGHT of each grid location
    WIDTH = 28
    HEIGHT = 28

    # This sets the margin between each cell
    MARGIN = 5

    # Initial value of dice as default
    dice = 0
    # dice = random.ranom

    def __init__(self):

        PieceA1 = Piece(1)
        PieceA2 = Piece(2)
        PiecesA = [PieceA1, PieceA2]

        PieceB1 = Piece(1)
        PieceB2 = Piece(2)
        PiecesB = [PieceB1, PieceB2]

        # attributes
        self.playerA = Player("GREEN", PiecesA, 'A')
        self.playerB = Player("RED", PiecesB, 'B')
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

        self.board.draw(2, 2, 3, 3, 12, 12, 11, 11, 0)

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

                    A = green1_route[self.playerA.pieces[0].current_pos]
                    B = green2_route[self.playerA.pieces[1].current_pos]
                    C = red1_route[self.playerB.pieces[0].current_pos]
                    D = red2_route[self.playerB.pieces[1].current_pos]
                    print(red1_route[self.playerB.pieces[0].current_pos])

                    print(A, B, C, D, pos)

                    if A == pos or B == pos or C == pos or D == pos and lock == 1:
                        if A == pos and player_turn == 0:
                            if self.playerA.pieces[0].state != 'home':
                                self.playerA.pieces[0].current_pos += self.dice
                                Piece = self.playerA.pieces[0]
                                new_position = green1_route[Piece.current_pos]
                                print("EDED", C[0], C[1], red1_route[self.playerB.pieces[0].current_pos])
                                self.board.draw(C[0], C[1], D[0], D[1], new_position[0], new_position[1], B[0], B[1],
                                                self.dice)
                                player_turn = 1  # keep alternating player turns
                            elif self.dice == 6:
                                if A == (12, 12):
                                    self.playerA.pieces[0].current_pos += 1
                                else:
                                    self.playerA.pieces[0].current_pos += self.dice + 1
                                Piece = self.playerA.pieces[0]
                                new_position = green1_route[Piece.current_pos]
                                self.playerA.pieces[0].state = 'safe'
                                self.board.draw(C[0], C[1], D[0], D[1], new_position[0], new_position[1], B[0], B[1],
                                                self.dice)

                        elif B == pos and player_turn == 0:
                            if self.playerA.pieces[1].state != 'home':
                                self.playerA.pieces[1].current_pos += self.dice
                                Piece = self.playerA.pieces[1]
                                new_position = green2_route[Piece.current_pos]
                                self.board.draw(C[0], C[1], D[0], D[1], A[0], A[1], new_position[0], new_position[1],
                                                self.dice)
                                player_turn = 1  # keep alternating player turns
                            elif self.dice == 6:
                                if A == (11, 11):
                                    self.playerA.pieces[1].current_pos += 1
                                else:
                                    self.playerA.pieces[1].current_pos += self.dice + 1
                                Piece = self.playerA.pieces[1]
                                new_position = green2_route[Piece.current_pos]
                                self.playerA.pieces[1].state = 'safe'
                                self.board.draw(C[0], C[1], D[0], D[1], A[0], A[1], new_position[0], new_position[1],
                                                self.dice)
                            pass
                            player_turn = 1  # keep alternating player turns

                        elif C == pos and player_turn == 1:

                            pass
                            player_turn = 0  # keep alternating player turns

                        elif D == pos and player_turn == 1:

                            pass
                            player_turn = 0  # keep alternating player turns

                        lock = 0   # the player can roll the dice now
                        self.dice = 0


                    # coordinates.append((row, column))
                    # Set that location to one
                    # grid[row][column] = 1
                    # print("Click ", pos, "Grid coordinates: ", row, column)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # User presses enter
                    print("REDRED", red1_route[self.playerB.pieces[0].current_pos])
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



    def main(self):

        self.render()


