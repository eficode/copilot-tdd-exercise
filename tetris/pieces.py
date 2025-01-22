from enum import Enum

class TetrominoType(Enum):
    I = 1
    O = 2
    T = 3
    S = 4
    Z = 5
    J = 6
    L = 7

class Piece:
    def __init__(self, tetromino_type):
        self.type = tetromino_type
        # For demonstration, store a shape as a list of coordinates or something similar
        # e.g., for an I piece, a simple placeholder could be:
        if self.type == TetrominoType.I:
            self.shape = [(0,0), (0,1), (0,2), (0,3)]
        else:
            self.shape = []
    
    def rotate(self):
        """Rotate the piece 90 degrees in place (placeholder)."""
        # TDD approach: implement later once you see the test fail
        pass
