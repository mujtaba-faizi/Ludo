from modules.Board import Board
from modules.Player import Player
from modules.Piece import Piece
import random
import pygame


class Ludo:

    @staticmethod
    def main():
        b = Board()
        # PieceA1 = Piece()
        # PieceA2 = Piece()
        # Pieces = [PieceA1, PieceA2]
        # playerA = Player("RED", Pieces, 'A')
        # PieceB1 = Piece()
        # PieceB2 = Piece()
        # Pieces = [PieceB1, PieceB2]
        # playerB = Player("GREEN", Pieces, 'B')

        b.render(2, 2, 3, 3, 12, 12, 11, 11, 0)

        # done = False
        # player = 0
        # while not done:
        #     for event in pygame.event.get():  # User did something
        #         if event.type == pygame.QUIT:  # If user clicked close
        #             done = True  # Flag that we are done so we exit this loop
        #         elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        #             # User presses enter
        #             dice = random.randint(0, 6)
        #             b.render(2, 2, 3, 3, 12, 12, 11, 11, dice)
        #             if player == 0:
        #                 pass
        #                 player = 1
        #             else:
        #                 pass
        #                 player = 0

        # print("Player A is Red\nPlayer B is Green")
        # while True:
        #     input("Player A's turn")
        #

