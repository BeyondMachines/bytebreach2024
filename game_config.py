# game_config.py
WORD_LIST = [
    "python", "programming", "computer", "algorithm", "database",
    "network", "software", "developer", "interface", "terminal"
]

MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    # ... more stages omitted for brevity
]
