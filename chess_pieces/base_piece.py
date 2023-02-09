class ChessPiece:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move_position(self, newposition):
        self.position = newposition
