def ceasar(let, sh):
    if let.isalpha():
        num = ord(let) + sh % 25
        if num > 122 or 90 < num < 97:
            num -= 25
        return chr(num) 
    return let
text = str(input("Введіть текст: "))
i = 0
for item in text:
    i += 1
    for item2 in item:
        print(ceasar(item2, i), end="")