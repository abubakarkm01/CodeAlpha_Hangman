# src/game.py
# Core Hangman game logic

import random

class HangmanGame:
    def __init__(self, secret_word, max_wrong=6):
        self.secret_word = secret_word.lower()
        self.max_wrong = max_wrong
        self.wrong_guesses = 0
        self.guessed_letters = []

    def guess(self, letter):
        letter = letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Enter only one alphabet letter.")
        if letter in self.guessed_letters:
            return None
        self.guessed_letters.append(letter)
        if letter not in self.secret_word:
            self.wrong_guesses += 1
            return False
        return True

    def display_progress(self):
        return " ".join([ch.upper() if ch in self.guessed_letters else "_" for ch in self.secret_word])

    def used_letters(self):
        return " ".join(sorted(set(self.guessed_letters))).upper() if self.guessed_letters else "-"

    def is_won(self):
        return all(ch in self.guessed_letters for ch in self.secret_word)

    def is_lost(self):
        return self.wrong_guesses >= self.max_wrong

    def lives_left(self):
        return self.max_wrong - self.wrong_guesses

def load_words_from_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return ["python", "flask", "pandas", "coding", "script"]

def choose_random_word(words):
    return random.choice(words)
