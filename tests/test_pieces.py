import pytest
from tetris.pieces import Piece, TetrominoType

def test_piece_creation():
    # Arrange / Act
    piece = Piece(TetrominoType.I)
    
    # Assert
    assert piece.type == TetrominoType.I
    # Typically, the "I" piece is 4 squares in a row
    assert len(piece.shape) == 4


def test_piece_rotation():
    piece = Piece(TetrominoType.I)
    
    original_shape = piece.shape.copy()
    piece.rotate()
    
    # We'll just check that the shape changed for demonstration
    # In real Tetris you'd have a more specific shape check
    assert piece.shape != original_shape
