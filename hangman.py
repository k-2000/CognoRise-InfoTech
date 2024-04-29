import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = ""
        self.guesses_left = 6
        self.guessed_letters = set()
        self.generate_word()

    def generate_word(self):
        self.word = random.choice(self.word_list).upper()

    def display_word_state(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        print(displayed_word)

    def display_hangman(self):
        hangman_figure = [
            "  ____ ",
            " |    |",
            " |    " + ("O" if self.guesses_left < 6 else ""),
            " |   " + ("/" if self.guesses_left < 5 else "") + ("|" if self.guesses_left < 4 else "") + ("\\" if self.guesses_left < 3 else ""),
            " |   " + ("/ " if self.guesses_left < 2 else "") + (" \\" if self.guesses_left < 1 else ""),
            " |",
            "|"
        ]
        for line in hangman_figure:
            print(line)

    def check_guess(self, guess):
        if guess.upper() in self.word:
            self.guessed_letters.add(guess.upper())
            print("Correct guess!")
        else:
            self.guesses_left -= 1
            print("Incorrect guess!")

    def check_win_loss(self):
        if all(letter in self.guessed_letters for letter in self.word):
            print("Congratulations! You won!")
            return True
        elif self.guesses_left == 0:
            print("Sorry, you lost. The word was:", self.word)
            return True
        return False

def main():
    word_list = ["PYTHON", "JAVA", "RUBY", "CPLUSPLUS", "JAVASCRIPT"]
    play_again = True
    while play_again:
        game = HangmanGame(word_list)
        while not game.check_win_loss():
            print("\nHangman:")
            game.display_hangman()
            print("\nWord:")
            game.display_word_state()
            guess = input("\nEnter your guess: ")
            game.check_guess(guess)
        play_again = input("\nDo you want to play again? (yes/no): ").lower() == "yes"

if __name__ == "__main__":
    main()
