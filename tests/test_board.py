import pytest
from tetris.board import Board

def test_board_initialization():
    # Arrange / Act
    board = Board(rows=20, columns=10)

    # Assert
    assert board.rows == 20
    assert board.columns == 10
    assert len(board.grid) == 20
    assert len(board.grid[0]) == 10


def test_board_is_cell_empty():
    board = Board(rows=20, columns=10)

    # We expect an empty board initially
    assert board.is_cell_empty(0, 0) is True
    assert board.is_cell_empty(19, 9) is True

    # Let's assume placing a block at (0,0) will make it non-empty
    board.place_block(0, 0, "X")
    board.place_block(19, 9, "Y")
    assert board.is_cell_empty(0, 0) is False
    assert board.is_cell_empty(19, 9) is False
