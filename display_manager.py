# display_manager.py
from game_config import HANGMAN_STAGES

class DisplayManager:
    @staticmethod
    def show_game_status(state, current_display):
        print("\n" * 50)  # Clear screen (sort of)
        print(HANGMAN_STAGES[6 - state.remaining_attempts])
        print(f"\nWord: {current_display}")
        print(f"Guessed letters: {', '.join(sorted(state.guessed_letters))}")
        print(f"Remaining attempts: {state.remaining_attempts}")
