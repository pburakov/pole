import random

MAX_SCORE = 100
ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЭЮЯ-"


def process_word(word: str):
    return word.replace("ё", "е").upper()


def load_vocabulary(filename: str) -> list:
    vocabulary = []
    with open(filename) as file:
        for line in file:
            word = line.replace("\n", "")
            vocabulary.append(word)
    return vocabulary


def calculate_ratio(word: str) -> int:
    unique_letters = set()
    for c in word:
        unique_letters.add(c)
    return int(MAX_SCORE / len(unique_letters))


def print_word(word: str, known_chars: set) -> None:
    for i in range(len(word)):
        if word[i] in known_chars:
            print(word[i], end='')
        else:
            print('-', end='')
    print()


def game_won(word: str, known_chars: set) -> bool:
    for c in word:
        if c not in known_chars:
            return False
    return True


def play(word: str):
    ratio = calculate_ratio(word)
    score = MAX_SCORE
    known_chars = set()
    guesses = set()
    print("Я загадал слово (одна попытка {} pts). Вот оно:".format(ratio))
    while not game_won(word, known_chars) and score > 0:
        print_word(word, known_chars)
        print("(Score: {}) Ваша буква:".format(score), end=' ')
        try:
            letter = input().upper()[0]
            if letter not in ALPHABET:
                raise ValueError()
        except:
            print("Ошибка...")
            continue
        print()
        if letter in guesses:
            print("Такая буква уже была...")
            continue
        guesses.add(letter)
        if letter in word:
            print("Есть такая буква!")
            known_chars.add(letter)
        else:
            score -= ratio
            print("Нет буквы '{}'... -{} pts".format(letter, ratio))
        print()
    if score > 0:
        print_word(word, known_chars)
        print("Вы выиграли!", end=" ")
    else:
        print("Вы проиграли...", end=" ")
    print("Final score: {} pts".format(score), end="\n\n")


if __name__ == '__main__':
    print("Загружаю словарь...", end="\n\n")
    try:
        vocabulary = load_vocabulary("word_rus.txt")
        word = vocabulary[random.randrange(len(vocabulary) - 1)]
        play(process_word(word))
    except:
        print("Ошибка!")
