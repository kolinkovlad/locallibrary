def foo(*a):
    z = len(a)
    if (z > 1):
        print("Кількість аргументів не може бути більше 1.\n format foo(argv1)" )
    b = a
    c = a
    v = b[0] + c[0] 
#    vv = len(v)
#    pg = b[0]
    if type(v) is str:
        print("Змінна: str")
    elif type(v) is int:
        print("Змінна: int")
    elif type(v) is float:
        print("Змінна: float")
    else: 
        print("Змінна: НЕВІДОМА!")
##   for v in range(0, vv):
#        print(pg[0])

print(foo("powefkwpoefk"))
##