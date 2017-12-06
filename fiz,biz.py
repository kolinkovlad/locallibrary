fiz = 4
biz = 7
for item in range (1,100):
    if (item % 7 == 0) and (item % 4 == 0):
        print("fizbiz", end=" ")
    elif (item % 4 == 0):
        print("fiz", end=" ")
    elif (item % 7 == 0):
        print("biz", end=" ")
    else:
        print(item, end=" ")
       
    