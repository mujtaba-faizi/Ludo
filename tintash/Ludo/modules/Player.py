import pickle


class Player:

    # Initializer / Instance Attributes
    def __init__(self, name, pieces, player):
        self.name = name
        self.pieces = pieces
        self.player = player

    def get_route(self, piece):
        if self.player == 'A':
            if piece == 1:
                with open('data/PlayerA_route.pkl', 'rb') as f:
                    route = pickle.load(f)
                    route.insert(0, (12, 12))
            else:
                with open('data/PlayerA_route.pkl', 'rb') as f:
                    route = pickle.load(f)
                    route.insert(0, (11, 11))
        else:
            if piece == 1:
                with open('data/PlayerB_route.pkl', 'rb') as f:
                    route = pickle.load(f)
                    route.insert(0, (2, 2))
            else:
                with open('data/PlayerB_route.pkl', 'rb') as f:
                    route = pickle.load(f)
                    route.insert(0, (3, 3))
        return route
