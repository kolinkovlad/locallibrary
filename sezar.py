import string


def key_enter():
    #ввід ключа для ссуву
    while True:
        key = str(input("Введіть ключ: "))
        if key.isalpha():
            print("Введіть число!")
            continue
        if 0 < int(key) < 26:
            return int(key)


def text_enter():
    #ввід незашифрованого тексту
    text = str(input("Введіть текст: "))
    if text.isalnum():
        return text
    else:
        print("Введіть текст: ")


def text_shift(letter, key):
    #шифрування(опрацювання кожної букви в text)
    cod = ord(letter)
    if 97 <= ord(letter) <= 122:
        cod = ord(letter) + key
        if cod > 122:
            cod - 26
    elif 65 <= ord(letter) <= 90:
        cod = ord(letter) + key
        if cod > 90:
            cod - 26
    return chr(cod)


def main():
    #вивід
    key = key_enter()
    letter = text_enter(item)
    for item in letter:
        print(text_shift(item, key), end="")

    if __name__ == "__main__":
        main()


assert text_shift("B", 13) == "O"
assert text_shift("!", 5) == "!"
assert text_shift('b', 13) == "o"
