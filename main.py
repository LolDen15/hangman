import stage
import random


class Hangman:
    words = []
    game_word = ...
    errors = 0
    word_progress = []

    def __init__(self):
        self.reset_errors()
        self.load_words()
        self.get_random_words()

    def load_words(self):
        file = "q.txt"
        with open(file, mode='r', encoding='utf-8') as f:
            for line in f:
                self.words.append(line.strip())

    def get_random_words(self):
        self.game_word = [i for i in random.choice(self.words)]
        self.word_progress = ['-' for _ in range(len(self.game_word))]

    def count_errors(self):
        self.errors += 1

    def reset_errors(self):
        self.errors = 0

    def try_answer_word(self, letter):
        if letter in self.game_word:
            for i in range(len(self.game_word)):
                if self.game_word[i] == letter:
                    self.word_progress[i] = self.game_word[i]
        else:
            self.count_errors()

    def show_stage_image(self):
        print(stage.stage[self.errors])

    def check_end_game(self):
        if self.errors >= stage.stage.__len__():
            return True
        else:
            return False


def main():
    while True:
        print('1.начать новую игру')
        print('2.выйти из приложения')
        res = input()
        if res == '1':
            word = Hangman()
            while True:
                if word.check_end_game():
                    word.get_random_words()
                    break
                word.show_stage_image()
                word.try_answer_word(input())
                print(word.word_progress)
        elif res == '2':
            exit()


if __name__ == '__main__':
    main()
