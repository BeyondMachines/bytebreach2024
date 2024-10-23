
# word_manager.py
import random
from game_config import WORD_LIST

class WordManager:
    @staticmethod
    def get_random_word():
        return random.choice(WORD_LIST).upper()
    
    @staticmethod
    def create_display(word, guessed_letters):
        return ' '.join(letter if letter in guessed_letters else '_' for letter in word)