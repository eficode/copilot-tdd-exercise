class TetrisGame:
    def __init__(self):
        # Start the game
        self.level = 1
        self.score = 0
        self.is_game_over = False
    
    def spawn_new_piece(self):
        """Spawn a new piece at the top of the board."""
        pass
    
    def move_piece_down(self):
        """Move the current piece down one row."""
        pass
    
    def check_line_clears(self):
        """Check for any full lines and clear them, update score, etc."""
        pass
    
    def update_game_state(self):
        """Central method to update the game state after each tick or user move."""
        pass
