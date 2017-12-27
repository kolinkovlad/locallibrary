def key_enter():
    while True:
        key = input("Введіть ключ шифрування -> ")
        if key.isdigit():
            if 0 < int(key) < 26:
                return int(key)
            else:
                print("<<УВАГА!!! Ключ шефрування не повинен бути більше 26 і менше 0>>")
        else:
            print("<<УВАГА!!! Ключ шефрування повинен бути цифрою!>>")


def text_enter():
    while True:
        text = input("Введіть текст для шефрування -> ")
        if 0 < len(text):
            return text
        else:
            print("<<УВАГА!!! Ви не ввели текст!>>")


def text_shift(text, key):
    for item in text:
        if item.islower():
            item = 96 + ((ord(item) - 96) + key) % 26
            return (chr(item))
        elif item.isupper():
            item = 64 + ((ord(item) - 64) + key) % 26
            return (chr(item))
        else:
            return (item)


def main():
    key = key_enter()
    some_text = text_enter()
    for item in some_text:
        print(text_shift(item, key), end="")


if __name__ == "__main__":
    main()

assert text_shift("B", 13) == "O"
assert text_shift("!", 5) == "!"
assert text_shift('b', 13) == "o"
