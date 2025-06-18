from random import choice
import uuid


class Main:
    def __init__(self, filename: str, attempts: int, alphabet: str):
        self.filename = filename
        self.games = {}
        self.attempts = attempts
        self.alphabet = alphabet


    def choose_random_word(self, player: str) -> int:
        for game in self.games.values():
            if game["player"] == player and game["status"] == "active":
                raise ValueError(f"У игрока {player} уже есть активная игра!")

        with open(self.filename, "r", encoding="utf-8") as file:
            words = file.read().split()

        game_id = uuid.uuid4()

        self.games[game_id] = {
            "game_id": game_id,
            "word": choice(words),
            "player": player,
            "attempts": self.attempts,
            "status": "active"
        }

        return game_id


    def get_game(self, game_id: int, player: str) -> dict:
        game = self.games.get(game_id)
        if not game:
            raise ValueError("Игра не найдена")
        if game["player"] != player:
            raise ValueError("Это не ваша игра!")
        return game


    def start_game(self, player: str, game_id: int):
        secret_word = self.games[game_id]["word"]
        print(
            'Добро пожаловать в виселицу на тему "виды спорта", '
            'потому что мы за здоровый образ жизни!'
        )
        print(f"У вас будет {self.attempts} попытки угадать секретное слово. Удачи!!")
        print("Слово:", "_" * len(secret_word))

        attempts = self.attempts
        guessed = []
        word_is_guessed = ""
        counter = attempts


        while counter > 0 and word_is_guessed != secret_word:
            while True:
                letter = input("Введите букву: ").lower()
                if letter not in self.alphabet:
                    print("Введите БУКВУ, пожалуйста.")
                else:
                    break

            if letter in guessed:
                print("Вы уже угадали эту букву.")
                continue

            if letter in secret_word:
                guessed.append(letter)
                positions = [i + 1 for i, l in enumerate(secret_word) if l == letter]
                print(f"Верно, буква '{letter}' на позициях: {', '.join(map(str, positions))}")
                current_word = "".join([ch if ch in guessed else "*" for ch in secret_word])
                print(current_word)
                word_is_guessed = current_word
            else:
                counter -= 1
                print(f"Не угадали. Количество оставшихся попыток: {counter}")
                if counter == 0:
                    print("Вы проиграли. Ответ:", secret_word)
                    self.games[game_id]["status"] = "lost"
                    return

        if word_is_guessed == secret_word:
            print("Поздравляем! Вы угадали слово:", secret_word)
            self.games[game_id]["status"] = "won"


def func() -> None:
    game = Main("input.txt", 3, "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    player = input("Введите имя игрока: ").strip()
    game_id = game.choose_random_word(player)
    data = game.get_game(game_id, player)
    #print(game.get_game(game_id, player="Susan"))


    if data is None:
        return
    game.start_game(player, game_id)


if __name__ == "__main__":
    func()
