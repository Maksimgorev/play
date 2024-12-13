from time import sleep
from delef import *
from delef2 import *
while True:
    print('''
    1 - начать войну
    2 - характеристика персонажа
    3 - характеристика стран
    4 - инвентарь
    5 - прокачка
    6 - больница
    7 - обучение
    8 - магазин
    9 - продажа
    10- заработок
    11 - благодарственное письмо
    12 - выйти из игры 
    ''')
    numder = int(input())

    if numder == 1:
        print("ждите обновления")

    elif numder == 2:
        print(plaer)

    elif numder == 3:
        print(vrag)

    elif numder == 4:
        if len(invent)<= 10:
            print(list(invent))
            if len(invent) > 3:
                for i in invent:
                    print(invent.list)
        elif len(invent)> 10:
            yes_no = input('''
            у вас много вещей надо избавится
            хотите?''')
            if yes_no == 'да':
                numder_1 = int(input("сколько хотите удалить вещей?"))
                for i in range(numder_1):
                    gan = input("что хотите удалить?")
                    invent.pop(gan)
            elif yes_no == "ничего":
                print("все осталось но вы ничего не положите")
            elif yes_no == 'нет':
                print("все осталось но вы ничего не положите")



    elif numder == 5:
        timeslepper()

    elif numder == 6:
        print(bolnica())
    
    elif numder == 7:
        rev = (delif1.prov(delif1.prowers()))
        invent.append(rev)

    elif numder == 8:
        print(things)
        a = input("хотите что - то купить :")
        if a == 'да':
            b = input("что?")
            c = (plaer['деньги'] - things[b]['summa'] )
            if c > 0:
                print(c)
                invent +=["мечь"]
                if len("ничего нету") in invent:
                    invent.remove('ничего нету')
            else:
                print("у вас недостаточно денег")

    elif numder == 9:
        while True:
            prog = input("что хотите продать:")
            sam = int(input("за сколько:"))
            if prog in things:
                if sam > (things[prog]['summa'] / 4):
                    print("за столько не продать")
                    d = input("хотите закончить продажу?")
                    if d == "да":
                        break
                else:
                    invent.remove(prog)
                    print("продано")
                    plaer['деньги'] = plaer['деньги'] + sam
            else:
                print("такого нету в магазине")
                break
    elif numder == 10:
        print(rabota(plaer['деньги'],rev))

    elif numder == 11:
        print(adc)

    elif numder == 12:
        exik()
        break