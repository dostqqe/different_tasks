from random import choice


class Main:
    def __init__(self, filename: str, attempts: int):
        self.filename = filename
        self.games = {}
        self.next_id = 1
        self._secret_word = None
        self.attempts = attempts


    def choose_random_word(self, player: str) -> int:
        for game in self.games.values():
            if game["player"] == player and game["status"] == "active":
                raise ValueError(f"У игрока {player} уже есть активная игра!")

        with open(self.filename, "r", encoding="utf-8") as file:
            words = file.read().split()
            game_id = self.next_id

        self.games[game_id] = {
            "word": choice(words),
            "player": player,
            "attempts": self.attempts,
            "status": "active"
        }

        self._secret_word = self.games[game_id]["word"]
        self.next_id += 1
        return game_id


    @property
    def get_word(self) -> str:
        return self._secret_word


    def get_game(self, game_id: int, player:str) -> dict | None:
        game = self.games.get(game_id)
        if not game:
            print("Игра не найдена!")
            return None
        if game["player"] != player:
            print("Это не ваша игра!")
            return None
        return game



    def attempts(self, game_id: int, player: str, word: str) -> str:
        game = self.get_game(game_id, player)
        if game["status"] != "active":
            raise ValueError("Игра уже завершена!")
        if word == game["word"]:
            game["status"] = "won"
            return "Вы угадали!"
        elif game["attempts"] <= 0:
            game["status"] = "lost"
            return f"Попытки кончились! Слово: {game['word']}"
        else:
            return f"Неверно! Осталось попыток: {game['attempts']}"


    def start_game(self):
        print(
            'Добро пожаловать в виселицу на тему "виды спорта", '
            'потому что мы за здоровый образ жизни!'
        )
        print(f"У вас будет {self.attempts} попытки угадать секретное слово. Удачи!!")
        print("Слово:", "_" * len(self._secret_word))
        play_game(self._secret_word, self.attempts)


class GetLetter:
    def __init__(self, alphabet: str) -> None:
        self.alphabet = alphabet

    def get_letter(self) -> str:
        while True:
            letter = input("Введите букву: ")
            if letter not in self.alphabet:
                print("Введите БУКВУ, пожалуйста.")
            else:
                return letter


class PrintWord:
    def __init__(self, secret_word: str, guessed_letters: list) -> None:
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


def play_game(secret_word: str, attempts_limit: int) -> None:
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


def func() -> None:

    new_game = Main("input.txt", 3)
    new_game.choose_random_word("Admin")
    data = new_game.get_game(1, "Admin")
    if data is None:
        return
    new_game.start_game()


if __name__ == "__main__":
    func()
