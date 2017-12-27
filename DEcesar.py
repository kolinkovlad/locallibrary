def de_ceasar(let, sh):
    if let.isalpha():
        num = ord(let) - sh 
        if num > 122 or 90 < num < 97:
            num += 25
        return chr(num) 
    return let
text = str(input("Введіть текст: "))
i = 0
for item in text:
    i += 1
    for item2 in item:
        print(de_ceasar(item2, i), end="")