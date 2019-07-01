from modules import Player


class Ludo:

    # Initializer / Instance Attributes
    def __init__(self, name, color):
        self.name = name
        self.color = color


pieces = int(input("Enter the number of pieces of each player(2-4) : "))
# if (pieces < 2 or pieces > 4):
#     print("Please enter a number 2-4:")
PlayerA = Player("Player A", pieces)
for piece in pieces:

PlayerB = Player("Player B", pieces)


