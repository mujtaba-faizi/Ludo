import pickle
from modules import Piece


class Player:

    # Initializer / Instance Attributes
    def __init__(self, name, Pieces, player):
        self.name = name
        self.Pieces = Pieces
        self.player = player

    def get_route(self):
        if self.player == 'A':
            with open('PlayerA_route.pkl', 'rb') as f:
                return pickle.load(f)
        else:
            with open('PlayerB_route.pkl', 'rb') as f:
                return pickle.load(f)

# Piec = Piece()
# Player = Player("koko",Piece,'A')