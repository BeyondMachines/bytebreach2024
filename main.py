# main.py
from game_engine import GameEngine

def main():
    game = GameEngine()
    while True:
        game.play_round()
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()