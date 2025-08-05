from random import choice
import uuid


class Main:
    def __init__(self, filename: str, attempts: int, alphabet: str):
        self.filename = filename
        self.games = {}
        self.attempts = attempts
        self.alphabet = alphabet

    def choose_random_word(self, player: str) -> uuid.UUID:
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
            "guessed_letters": [],
            "guessed_word": [],
            "status": "active",
        }

        return game_id

    def get_game(self, game_id: uuid.UUID, player: str) -> dict:
        game = self.games.get(game_id)
        if not game:
            raise ValueError("Игра не найдена")
        if game["player"] != player:
            raise ValueError("Это не ваша игра!")
        return game

    def attempt_to_guess(
        self, letter: str, game_id: uuid.UUID, player
    ):  #    letter, game_id, player
        game = self.get_game(game_id, player)
        if game["status"] != "active":
            return "Игра уже завершена"
        if letter not in game_instance.alphabet:
            return "Введите БУКВУ"
        if letter in game["guessed_letters"]:
            return "Вы уже угадали эту букву"

        secret_word = game["word"]
        if letter in secret_word:
            game["guessed_letters"].append(letter)
            positions = [i + 1 for i, l in enumerate(secret_word) if l == letter]
            message = f"Верно, буква '{letter}' на позициях: {', '.join(map(str, positions))}"
            current_word = "".join(
                [ch if ch in game["guessed_letters"] else "*" for ch in secret_word]
            )
            if current_word == game["word"]:
                game["status"] = "won"
                return f"Поздравляем! Вы угадали слово: {secret_word}"
            return f"{message}\n{current_word}"
        else:
            game["attempts"] -= 1
            message = f"Не угадали. Количество оставшихся попыток: {game["attempts"]}"
            current_word = "".join(
                [ch if ch in game["guessed_letters"] else "*" for ch in secret_word]
            )

            if game["attempts"] == 0:
                game["status"] = "lost"
                return f"Вы проиграли. Ответ: {game["word"]}"
            return f"{message}\n{current_word}"


def func(instance):
    player = input("Введите имя игрока: ").strip()
    game_id = instance.choose_random_word(player)
    secret_word = instance.games[game_id]["word"]
    try:
        data = instance.get_game(game_id, player)
    except ValueError as e:
        print(e)
        return

    print(
        'Добро пожаловать в виселицу на тему "виды спорта", '
        "потому что мы за здоровый образ жизни!"
    )
    print(f"У вас будет {instance.attempts} попытки угадать секретное слово. Удачи!!")
    print("Слово:", "*" * len(secret_word))

    while True:
        letter = input("Введите букву: ").lower()
        result = instance.attempt_to_guess(letter, game_id, player)
        print(result)
        game = instance.games[game_id]
        if game["status"] in ("won", "lost"):
            break


if __name__ == "__main__":
    game_instance = Main("input.txt", 3, "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    func(game_instance)
