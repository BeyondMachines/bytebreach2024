# game_state.py
from game_config import MAX_ATTEMPTS

class GameState:
    def __init__(self):
        self.word = ""
        self.guessed_letters = set()
        self.remaining_attempts = 0
        
    def initialize_game(self, word):
        self.word = word
        self.guessed_letters = set()
        self.remaining_attempts = MAX_ATTEMPTS
        
    def is_game_won(self):
        return all(letter in self.guessed_letters for letter in self.word)
    
    def is_game_lost(self):
        return self.remaining_attempts <= 0