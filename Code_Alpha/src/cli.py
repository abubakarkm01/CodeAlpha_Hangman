# src/cli.py
# from src.game import HangmanGame, load_words_from_file, choose_random_word
import os
from game import HangmanGame, load_words_from_file, choose_random_word

def play():
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "words.txt")
    words = load_words_from_file(data_file)
    secret = choose_random_word(words)

    # Debug line (put it exactly here)
    print(f"DEBUG: secret_word = '{secret}'")

    game = HangmanGame(secret)

def get_valid_guess(already_guessed):
    while True:
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter only one alphabet letter.")
            continue
        if guess in already_guessed:
            print("You already tried this letter.")
            continue
        return guess

def play():
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "words.txt")
    words = load_words_from_file(data_file)
    secret = choose_random_word(words)
    game = HangmanGame(secret)

    print("=== Hangman Game ===")
    print("Lives: 6")
    print(game.display_progress())

    while not game.is_won() and not game.is_lost():
        print(f"\nLives left: {game.lives_left()}")
        print(f"Used letters: {game.used_letters()}")
        guess = get_valid_guess(game.guessed_letters)
        result = game.guess(guess)
        if result is None:
            print(" Already guessed this one.")
        elif result:
            print("Correct!")
        else:
            print("Wrong!")
        print(game.display_progress())

    if game.is_won():
        print(f"\n You WIN! The word was: {secret.upper()}")
    else:
        print(f"\n You LOSE! The word was: {secret.upper()}")

if __name__ == "__main__":
    play()

