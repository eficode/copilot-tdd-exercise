import pytest
from tetris.game import TetrisGame

def test_game_initial_state():
    game = TetrisGame()
    
    # We expect the game to start at level 0 or 1, with a score of 0
    # Adjust the expectations to match your design
    assert game.level == 1
    assert game.score == 0
    assert game.is_game_over is False
