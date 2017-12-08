with open("alice.txt", 'r') as f:
    text = str(f.read())
list_f = []
text2 = text.replace(" ", "")
text1 = text.replace("\n", "")
text3 = text.split(".")
r_text3 = text1
#list_b = list_f.append(text)
#dict_t = {}
#pk = 0
print("<< Кількість символів в реченях:", len(r_text3), ">>")
print("<< Кількість символів в тексті(З пробілами): ", len(text), ">>")
print("<< Кількість символів в тексті(Без пробілів): ", len(text2), ">>")
print("<<Найдовше слово в тексті:",max(text.split(), key=lambda g: len(g)), ">>")
print("<<Найкоротше слово в тексті:",min(text.split(), key=lambda g: len(g)), ">>")
#for i in list_b:
#    if i in list_b:
#      pk += 1
#      dict_v = dict_t.a
      
 