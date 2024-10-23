# input_handler.py
class InputHandler:
    @staticmethod
    def get_letter():
        while True:
            guess = input("\nGuess a letter: ").upper()
            if len(guess) == 1 and guess.isalpha():
                return guess
            print("Please enter a single letter.")