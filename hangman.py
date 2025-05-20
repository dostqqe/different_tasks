from random import choice


class WordChooser():
    def __init__(self, filename, attempts):
        self.filename = filename

    def choose_random_word(self) -> str:
        with open(self.filename, "r", encoding="utf-8") as file:
            words = file.read().split()
        return choice(words)

class NewGame():
    def __init__(self, attempts, secret_word):
        self.attempts = attempts
        self.secret_word = secret_word

    def hello(self) -> str:
        print('Добро пожаловать в виселицу на тему "виды спорта", потому что мы за здоровый образ жизни!')
        print(f"У вас будет {self.attempts} попытки угадать секретное слово. Удачи!!")
        print("Слово:", '_' * len(self.secret_word))
        return self.secret_word

class GetLetter():
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def get_letter(self) -> str:
        while True:
            letter = input("Введите букву: ")
            if letter not in self.alphabet:
                print("Введите БУКВУ, пожалуйста.")
            else:
                return letter

class PrintWord():
    def __init__(self, secret_word, guessed_letters):
        self.secret_word = secret_word
        self.guessed_letters = guessed_letters

    def print_word(self) -> str:
        current_letters = []
        for i in self.secret_word:
            if i in self.guessed_letters:
                current_letters.append(i)
            else:
                current_letters.append("*")
        return "".join(current_letters)


def check_letter_in_word(secret: str, guessed: list, letter: str) -> bool:
    if letter in secret:
        for i in range(len(secret)):
            if secret[i] == letter:
                guessed.append(letter)
                print(f"Верно, эта буква на {i + 1} месте")
                return True
    return False

def play_game(secret_word: str, attempts_limit: int):
    counter = attempts_limit
    guessed = []
    word_is_guessed = ""

    while counter > 0 and word_is_guessed != secret_word:
        letter = GetLetter("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
        get_letter = letter.get_letter()

        if get_letter in guessed:
            print("Вы уже угадали эту букву.")
            continue
        if check_letter_in_word(secret_word, guessed, get_letter):
            made_word = PrintWord(secret_word, guessed)
            current_word = made_word.print_word()
            print(current_word)
            word_is_guessed = current_word
        else:
            counter -= 1
            print(f"Не угадали. Количество оставшихся попыток: {counter}")
            if counter == 0:
                print("Вы проиграли. Ответ:", secret_word)
                return

    if word_is_guessed == secret_word:
        print("Поздравляем! Вы угадали слово:", secret_word)

def func():
    chooser = WordChooser("input.txt", 3)
    secret_word = chooser.choose_random_word()
    new_game = NewGame(3, secret_word=secret_word)
    game = new_game.hello()
    play_game(secret_word, 3)

if __name__ == "__main__":
    func()
