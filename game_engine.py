# game_engine.py
from word_manager import WordManager
from input_handler import InputHandler
from game_state import GameState
from display_manager import DisplayManager

class GameEngine:
    def __init__(self):
        self.word_manager = WordManager()
        self.input_handler = InputHandler()
        self.display_manager = DisplayManager()
        self.game_state = GameState()
    
    def play_round(self):
        word = self.word_manager.get_random_word()
        self.game_state.initialize_game(word)
        
        while True:
            current_display = self.word_manager.create_display(
                self.game_state.word, 
                self.game_state.guessed_letters
            )
            
            self.display_manager.show_game_status(self.game_state, current_display)
            
            if self.game_state.is_game_won():
                print(f"\nCongratulations! You won! The word was {self.game_state.word}")
                break
                
            if self.game_state.is_game_lost():
                print(f"\nGame Over! The word was {self.game_state.word}")
                break
            
            guess = self.input_handler.get_letter()
            
            if guess in self.game_state.guessed_letters:
                print("\nYou already guessed that letter!")
                continue
                
            self.game_state.guessed_letters.add(guess)
            
            if guess not in self.game_state.word:
                self.game_state.remaining_attempts -= 1
                print("\nIncorrect guess!")
            else:
                print("\nCorrect guess!")