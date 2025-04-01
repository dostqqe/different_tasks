from random import choice

#alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#list_of_words = ["плавание", "бег", "бокс", "велоспорт", "волейбол", "коньки"]
#secret_word = choice(list_of_words)
#attempts_limit = 3
#counter = attempts_limit
#guessed = []
#word_is_guessed = ""

def welcome(attempts_limit_thing: int, list_of_words: list) -> str:
    meaning = choice(list_of_words)
    print('Добро пожаловать в виселицу на тему "виды спорта", потому что мы за здоровый образ жизни!')
    print(f"У вас будет {attempts_limit_thing} попытки угадать секретное слово. Удачи!!")
    print("Слово:", '_' * len(meaning))
    return meaning

meaning = welcome(3, ["плавание", "бег", "бокс", "велоспорт", "волейбол", "коньки"])

def print_word(guessed_letters: str, secret_words: str) -> str:
    current_letters = []
    for i in secret_words:
        if i in guessed_letters:
            current_letters.append(i)
        else:
            current_letters.append("*")
    return "".join(current_letters)

def game_process(counter: int, secret_word: str):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    guessed = []
    word_is_guessed = ""
    while counter > 0 and word_is_guessed != secret_word:
        letter = input("Введите букву:")
        if letter not in alphabet:
            print("Введите БУКВУ")
        elif letter in guessed:
            print("Вы уже угадали эту букву")

        elif letter in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    guessed.append(letter)
                    print(f"Верно, эта буква на {i + 1} месте")
                    print(print_word(guessed))
                    word_is_guessed = print_word(guessed)
        else:
            counter -= 1
            print(f"Количество оставшихся попыток: {counter}")
        return word_is_guessed, counter

def check(secret_word: str) -> bool:
    if word_is_guessed == secret_word:
        print("Вы угадали слово")
    elif counter == 0:
        print("Вы проиграли. Ответ:", secret_word)



def func():
    welcome(3, ["плавание", "бег", "бокс", "велоспорт", "волейбол", "коньки"])
    game_process(3, meaning)
    check(meaning, )


if __name__  == "__main__":
    func()
