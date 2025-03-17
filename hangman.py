from random import choice

alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
            "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
listOfWords = ['плавание', 'бег', 'бокс', 'велоспорт', 'волейбол', 'коньки']
secretWord = choice(listOfWords)
count = 3
guessed = []
viktory = ''


def print_word(secretword, guessed_letters):
    current_letters = []
    for i in secretWord:
        if i in guessed_letters:
            current_letters.append(i)
        else:
            current_letters.append("*")
    return "".join(current_letters)


print('Добро пожаловать в виселицу на тему "виды спорта", потому что мы за здоровый образ жизни!')
print("У вас будет 3 попытки угадать секретное слово. Удачи!!")
print("Слово:", '_' * len(secretWord))

while count > 0 and viktory != secretWord:
    letter = input("Введите букву:")
    if letter not in alphabet:
        "Введите БУКВУ"
    elif letter in guessed:
        print("Вы уже угадали эту букву")
    elif letter in secretWord:
        for i in range(len(secretWord)):
            if secretWord[i] == letter:
                guessed.append(letter)
                print("Верно, эта буква на ", i+1, "месте")
                print(print_word(secretWord, guessed))
                viktory = print_word(secretWord, guessed)
    else:
        count -=  1
        if count == 2:
            print("У вас осталось 2 попытки")
        else: print("У вас осталась одна попытка")

if viktory == secretWord:
    print("Вы угадали слово")
elif count == 0: print("Вы проиграли. Ответ:", secretWord)
