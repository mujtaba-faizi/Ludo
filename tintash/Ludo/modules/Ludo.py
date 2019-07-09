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

    player_turn = 'green'
    lock = 0

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

        # all routes
        self.green1_route = self.playerA.get_route(1)
        self.green2_route = self.playerA.get_route(2)
        self.red1_route = self.playerB.get_route(1)
        self.red2_route = self.playerB.get_route(2)

    def get_new_positions(self):

        # get the updated positions of all pieces
        a = self.green1_route[self.playerA.pieces[0].current_pos]
        b = self.green2_route[self.playerA.pieces[1].current_pos]
        c = self.red1_route[self.playerB.pieces[0].current_pos]
        d = self.red2_route[self.playerB.pieces[1].current_pos]
        return a, b, c, d

    def kill(self, position):

        a, b, c, d = self.get_new_positions()
        if self.player_turn == 'green':
            if position == c and self.playerB.pieces[0].state == 'unsafe':
                self.playerB.pieces[0].killed()
            elif position == d and self.playerB.pieces[1].state == 'unsafe':
                self.playerB.pieces[1].killed()
        else:
            if position == a and self.playerA.pieces[0].state == 'unsafe':
                self.playerA.pieces[0].killed()
            elif position == b and self.playerA.pieces[1].state == 'unsafe':
                self.playerA.pieces[1].killed()

    def movement(self, position, home, player1, route, piece_no):

        if self.dice == 6:
            if position == home:
                if player1.pieces[piece_no].state == 'home':
                    player1.pieces[piece_no].move(1)
                else:
                    player1.pieces[piece_no].move(6)
            else:
                player1.pieces[piece_no].move(6)
            piece = player1.pieces[piece_no]
            new_position = route[piece.current_pos]
            self.kill(new_position)
            self.lock = 0    # the player can roll the dice now
            return new_position

        elif player1.pieces[piece_no].state != 'home':
            player1.pieces[piece_no].move(self.dice)
            piece = player1.pieces[piece_no]
            new_position = route[piece.current_pos]
            self.kill(new_position)
            if self.player_turn == 'green':
                self.player_turn = 'red'
            else:
                self.player_turn = 'green'
            self.lock = 0    # the player can roll the dice now
            return new_position

        return False

    def render(self):

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        grid = [[0 for x in range(15)] for y in range(15)]    # Add an empty array that will hold each cell in this row

        # Set row 1, cell 5 to one. (Remember rows and
        # column numbers start at zero.)
        grid[1][5] = 1

        # Loop until the user clicks the close button.
        done = False

        self.board.draw(2, 2, 3, 3, 12, 12, 11, 11, 0, 1, self.player_turn)     # initial state of board

        # -------- Main Controller Implementation -----------
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

                    a, b, c, d = self.get_new_positions()

                    if (a == pos or b == pos or c == pos or d == pos) and self.lock == 1:

                        if a == pos and self.player_turn == 'green':
                            new_position = self.movement(a, (12, 12), self.playerA, self.green1_route, 0)
                            if new_position is not False:
                                a, b, c, d = self.get_new_positions()
                                self.board.draw(c[0], c[1], d[0], d[1], new_position[0], new_position[1], b[0], b[1],
                                                self.dice, self.lock, self.player_turn)

                        elif b == pos and self.player_turn == 'green':
                            new_position = self.movement(b, (11, 11), self.playerA, self.green2_route, 1)
                            if new_position is not False:
                                a, b, c, d = self.get_new_positions()
                                self.board.draw(c[0], c[1], d[0], d[1], a[0], a[1], new_position[0], new_position[1],
                                                self.dice, self.lock, self.player_turn)

                        elif c == pos and self.player_turn == 'red':
                            new_position = self.movement(c, (2, 2), self.playerB, self.red1_route, 0)
                            if new_position is not False:
                                a, b, c, d = self.get_new_positions()
                                self.board.draw(new_position[0], new_position[1], d[0], d[1], a[0], a[1], b[0], b[1],
                                                self.dice, self.lock, self.player_turn)

                        elif d == pos and self.player_turn == 'red':
                            new_position = self.movement(d, (3, 3), self.playerB, self.red2_route, 1)
                            if new_position is not False:
                                a, b, c, d = self.get_new_positions()
                                self.board.draw(c[0], c[1], new_position[0], new_position[1], a[0], a[1], b[0], b[1],
                                                self.dice, self.lock, self.player_turn)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # User presses enter
                    if self.lock == 0:
                        self.dice = random.randint(1, 6)
                        self.board.draw(self.red1_route[self.playerB.pieces[0].current_pos][0],
                                        self.red1_route[self.playerB.pieces[0].current_pos][1],
                                        self.red2_route[self.playerB.pieces[1].current_pos][0],
                                        self.red2_route[self.playerB.pieces[1].current_pos][1],
                                        self.green1_route[self.playerA.pieces[0].current_pos][0],
                                        self.green1_route[self.playerA.pieces[0].current_pos][1],
                                        self.green2_route[self.playerA.pieces[1].current_pos][0],
                                        self.green2_route[self.playerA.pieces[1].current_pos][1],
                                        self.dice,
                                        self.lock,
                                        self.player_turn
                                        )

                        # to avoid having to click in-order to proceed when all pieces are at home
                        if self.player_turn == 'green' and self.dice != 6 and \
                                self.playerA.pieces[0].state == 'home' and self.playerA.pieces[1].state == 'home':
                            self.player_turn = 'red'
                            self.lock = 0
                        elif self.player_turn == 'red' and self.dice != 6 and \
                                self.playerB.pieces[0].state == 'home' and self.playerB.pieces[1].state == 'home':
                            self.player_turn = 'green'
                            self.lock = 0
                        else:
                            self.lock = 1

    def main(self):
        self.render()
