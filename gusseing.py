condition = True
while (condition):
    num = int(input("guesse the number: "))
    if(num == 76):
        condition = False
        print("congrulation u guess correct number")
    elif(num >76):
        print("ur no. is larger")
    elif(num<76 and num >0):
        print("ur no. is smaller")
    elif(num+-0):
        print("ur quting the game")