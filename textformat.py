# f = open('austen.txt')
# text = f.read()
# f.close()


def read_from_file():
    with open('austen.txt') as f:
        text = str(f.read())
    return text


def func1(listabzats):
    # середнє значення символів у абзаці
    return sum(listabzats) / len(listabzats)


# print(func(listnew))



def func2(listsentence):
    # середнє значення символів у реченні
    return sum(listsentence) / len(listsentence)


# print(func(listnew2))

def reformat(text):
    symbols = ',!?[]{}*:_;"'
    for item in symbols:
        text = text.replace(item, '')
    return text




def minmaxword(text):
    word = ""
    word1 = "  "
    listword = [item for item in text.split()]
    for item in listword:
        if len(item) > len(word):
            word = item
        elif len(item) <= len(word1):
            word1 = item
    return print("Найдовше слово: ", word), print("Найкоротше слово: ", word1)



def main():
    text = read_from_file()
    text = reformat(text)
    text = minmaxword(text)
    listabzats = [len(item) for item in text.split("\n\n")]
    listsentence = [len(item) for item in text.split(".")]
    listword = [item for item in text.split()]
    """Чому він на ці 3 рядки що вище свариться на те що локальна змінна не використовується і те що це кортеж,
    який не є ітерабельним, все б нічого але це список, а не кортеж"""
    print(text)
    print(func1(listnew))
    print(func2(listnew2))


main()
