from random import choice
import uuid


class Main:
    def __init__(self, filename: str, attempts: int, alphabet: str):
        self.filename = filename
        self.games = {}
        self.game_id = None
        self._secret_word = None
        self.attempts = attempts
        self.alphabet = alphabet


    def choose_random_word(self, player: str) -> int:
        for game in self.games.values():
            if game["player"] == player and game["status"] == "active":
                raise ValueError(f"У игрока {player} уже есть активная игра!")

        with open(self.filename, "r", encoding="utf-8") as file:
            words = file.read().split()

        game_id = int(uuid.uuid4())

        self.games[game_id] = {
            "word": choice(words),
            "player": player,
            "attempts": self.attempts,
            "status": "active"
        }

        self.game_id = game_id
        self.secret_word = self.games[game_id]["word"]
        return self.game_id


    def get_game(self, game_id: int, player:str) -> dict:
        game = self.games.get(game_id)
        if not game:
            raise ValueError("Игра не найдена")
        if game["player"] != player:
            raise ValueError("Это не ваша игра!")
        return game


    def use_attempts(self, game_id:int, player: str,) -> str:
        game = self.get_game(game_id, player)

        if game["status"] != "active":
            raise ValueError("Игра уже завершена!")
        while True:
            letter = input("Введите букву: ").lower()
            if letter not in self.alphabet:
                print("Введите БУКВУ, пожалуйста.")
            else:
                return letter


    def start_game(self, player):
        print(
            'Добро пожаловать в виселицу на тему "виды спорта", '
            'потому что мы за здоровый образ жизни!'
        )
        print(f"У вас будет {self.attempts} попытки угадать секретное слово. Удачи!!")
        print("Слово:", "_" * len(self.secret_word))
        play_game(self, player)


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


def play_game(main: Main, player: str):
    game_id = main.game_id
    secret_word = main.secret_word
    counter = main.games[game_id]["attempts"]
    guessed = []
    word_is_guessed = ""

    while counter > 0 and word_is_guessed != secret_word:
        result = main.use_attempts(game_id, player)
        print(result)

        if result in guessed:
            print("Вы уже угадали эту букву.")
            continue
        if check_letter_in_word(secret_word, guessed, result):
            made_word = PrintWord(secret_word, guessed)
            current_word = made_word.print_word()
            print(current_word)
            word_is_guessed = current_word
        else:
            counter -= 1
            main.games[game_id]["attempts"] = counter
            print(f"Не угадали. Количество оставшихся попыток: {counter}")
            #print(main.games[game_id]) проверка обновления словаря
            if counter == 0:
                print("Вы проиграли. Ответ:", secret_word)
                return

    if word_is_guessed == secret_word:
        main.games[game_id]["status"] = "complete"
        print("Поздравляем! Вы угадали слово:", secret_word)


def func() -> None:
    player = input("Введите имя игрока: ").strip()
    new_game = Main("input.txt", 3, "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    game_id = new_game.choose_random_word(player)
    data = new_game.get_game(game_id, player)
    #print(new_game.get_game(game_id, player))
    #print(new_game.get_game(game_id, player="Susan")) проверка для ошибки

    if data is None:
        return
    new_game.start_game(player)


if __name__ == "__main__":
    func()
