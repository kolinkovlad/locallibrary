def key_enter():
    while True:
        key = str(input("Enter key:"))
        if key.isalpha():
            print("The key must be in 1-26 figers")
            continue
        if 0 < int(key)<26:
            return int(key)
        else:
            print("The key must be in 1-26 region.")

def text_enter():
    text= str(input('Enter text: '))
    if len(text)==0:
        print ('len(text)=0')
    return text

def text_shift(letter, key):
    if letter in " ,.!?;:":
        print ("not ")
    letter = ord(letter)
    return chr(letter+key)

def main():
    key = key_enter()
    some_text = text_enter()
    for item in some_text:
        print(text_shift(key, item), end="")

print(text_shift('w',4))
# if __name__== "__main__":
#     main()
#
# assert text_shift("B", 13) == "O"
# assert text_shift("!", 5) == "!"
# assert text_shift('b', 13) == "o"
