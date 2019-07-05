class Piece:

    # Initializer / Instance Attributes
    def __init__(self, name):
        self.current_pos = 0
        self.state = 'home'
        self.name = name

    def move(self, increment):
        if self.state is not 'home':
            if (self.current_pos + increment) > 56:    # Cant go beyond the board tiles
                return
            elif (self.current_pos + increment) == 56:    #
                self.state = 'win'
                return
            self.current_pos += increment
            if self.current_pos == (8 or 13 or 21 or 26 or 34 or 39 or 47):
                self.state = 'safe'
            else:
                self.state = 'unsafe'
        else:
            self.current_pos = 1
            self.state = 'safe'
