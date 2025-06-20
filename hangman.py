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


    def attempt_to_guess(self, letter, secret_word, counter, guessed):
        if letter not in self.alphabet:
            return "Введите БУКВУ, пожалуйста.", guessed, counter, None
        elif letter in guessed:
            return "Вы уже угадали эту букву.", guessed, counter, None
        elif letter in secret_word:
            guessed.append(letter)
            positions = [i + 1 for i, l in enumerate(secret_word) if l == letter]
            message = f"Верно, буква '{letter}' на позициях: {', '.join(map(str, positions))}"
            current_word = "".join([ch if ch in guessed else "*" for ch in secret_word])
            return message, guessed, counter, current_word
        else:
            counter -= 1
            message = f"Не угадали. Количество оставшихся попыток: {counter}"
            current_word = "".join([ch if ch in guessed else "*" for ch in secret_word])
            return message, guessed, counter, current_word


def func(instance):
    attempts = instance.attempts
    counter = attempts
    guessed = []


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
        'потому что мы за здоровый образ жизни!'
    )
    print(f"У вас будет {instance.attempts} попытки угадать секретное слово. Удачи!!")
    print("Слово:", "*" * len(secret_word))

    word_is_guessed = "*" * len(secret_word)
    while counter > 0 and word_is_guessed != secret_word:
        letter = input("Введите букву: ").lower()
        message, guessed, counter, word_is_guessed = instance.attempt_to_guess(letter, secret_word, counter, guessed)
        print(message)
        print(word_is_guessed)

    if word_is_guessed == secret_word:
        print("Поздравляем! Вы угадали слово:", secret_word)
        instance.games[game_id]["status"] = "won"
    else:
        print("Вы проиграли. Ответ:", secret_word)
        instance.games[game_id]["status"] = "lost"


if __name__ == "__main__":
    game_instance = Main("input.txt", 3, "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    func(game_instance)
