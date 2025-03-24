from random import choice

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
list_of_words = ["плавание", "бег", "бокс", "велоспорт", "волейбол", "коньки"]
secret_word = choice(list_of_words)
attempts_limit = 3
counter = attempts_limit
guessed = []
word_is_guessed = ""

def print_word(guessed_letters: str) -> str:
    current_letters = []
    for i in secret_word:
        if i in guessed_letters:
            current_letters.append(i)
        else:
            current_letters.append("*")
    return "".join(current_letters)


print('Добро пожаловать в виселицу на тему "виды спорта", потому что мы за здоровый образ жизни!')
print(f"У вас будет {attempts_limit} попытки угадать секретное слово. Удачи!!")
print("Слово:", '_' * len(secret_word))

while counter > 0 and word_is_guessed != secret_word:
    letter = input("Введите букву:")
    if letter not in alphabet:
        print("Введите БУКВУ")
        continue    
    if letter in guessed:
        print("Вы уже угадали эту букву")
        continue
    if letter in range(len(secret_word)):
        for i in secret_word:
            if secret_word[i] == letter:
                guessed.append(letter)
                print("Верно, эта буква на ", i+1, "месте")
                print(print_word(guessed))
                word_is_guessed = print_word(guessed)
    else:
        counter -=  1
        print(f"Количество оставшихся попыток: {counter}")

if word_is_guessed == secret_word:
    print("Вы угадали слово")
if counter == 0: 
    print("Вы проиграли. Ответ:", secret_word)
