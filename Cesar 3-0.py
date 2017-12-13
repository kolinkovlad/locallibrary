def key_enter():
    while True:
        key = input("Введіть rлюч шефрування ")
        if key.isdigit():
            if 0 < int(key) < 26:
                print('Ключ шефрування ', key)
                return int(key)
            else:
                print("Ключ шефрування повинен бути від 1 до 26")
        else:
            print('Ключ шефрування мітить літери ')

def text_enter():
    while True:
        text = input("Введіть текст для шефрування >>> ")
        if 0 < len(text):
            return text
        else:
            print('Це поле не повино бути порожнім ')

       
def text_shift(text, key):
    for i in text:
        if i.islower():
            i = 96 + ((ord(i) - 96) + key) % 26
            return (chr(i))
        elif i.isupper():
            i = 64 + ((ord(i) - 64) + key) % 26
            return (chr(i))
        else:
            return (i)

    
def main():
    key = key_enter()
    some_text = text_enter()
    for i in some_text:
        print(text_shift(i, key), end = "")


if __name__== "__main__":
    main()

assert text_shift("B", 13) == "O", 'Якщо ...'
assert text_shift("!", 5) == "!"
assert text_shift('b', 13) == "o"
