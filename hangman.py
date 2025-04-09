from random import choice

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
list_of_words = ["плавание", "бег", "бокс", "велоспорт", "волейбол", "коньки"]
attempts_limit = 3

def choose_random_word(words):
    return choice(words)

def hello(attempts: int, our_word: str) -> str:
    print('Добро пожаловать в виселицу на тему "виды спорта", потому что мы за здоровый образ жизни!')
    print(f"У вас будет {attempts} попытки угадать секретное слово. Удачи!!")
    print("Слово:", '_' * len(our_word))

def print_word(secret: str, guessed_letters: str) -> str:
    current_letters = []
    for i in secret:
        if i in guessed_letters:
            current_letters.append(i)
        else:
            current_letters.append("*")
    return "".join(current_letters)

def get_letter() -> str:
    while True:
        letter = input("Введите букву:").lower()  # Приводим к нижнему регистру
        if letter not in alphabet:
            print("Введите БУКВУ, пожалуйста.")
        else:
            return letter

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

    hello(attempts_limit, secret_word)

    while counter > 0 and word_is_guessed != secret_word:
        letter = get_letter()

        if letter in guessed:
            print("Вы уже угадали эту букву.")
            continue
        if check_letter_in_word(secret_word, guessed, letter):
            current_word = print_word(secret_word, "".join(guessed))
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
    secret_word = choose_random_word(list_of_words)
    play_game(secret_word, attempts_limit)

if __name__ == "__main__":
    func()
