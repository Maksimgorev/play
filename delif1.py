from day_Shop import *
from time import sleep
from random import randint
def psix(invent):
    a = int(input ('1+2'))
    b = int(input("сколько у тебя ног и рук"))
    r = input("как называется орган который вы видите ")

    if  (a == 3) and (b == 2) and (r == 'глаза'):
        invent.append('справка от терапевта то что психически здоров')
        if len("ничего нету") in invent:
            invent.removе('ничего нету')
    else:
        return ("вы не прошли")

def hped():
    a = ("что у вас болит?")
    b = ["врач очень сильно стрался но все таки не смог все таки вам помочь ",
    '''вам врач помог хотя очень сильно хотел устал и теперь требует с вас 50 рублей''',
    'хотели как лучше но получилось как всегда']
    c = b[randint(0,2)]
    return c

def prov():
    print(prowers)
    prower =  input("какое образование вы хотите:")
    if prower == "учитель":
        tetche = input('''какой учитель?
        учитель математики
        учитель физики
        учитель физической культуры
        учитель химии
        учитель информатики
        учитель обж
        учитель географии
        учитель истории
        ''')

        a = input("быстро хотите?")
        if a == "да":
            print("а вот не получится, сиди жди когда закончишь образование")
            sleep(1)
            print("обучение закончивается ... 0%")
            sleep(5)
            print("обучение закончено на 10%")
            sleep(5)
            print("обучение закончено на 20%")
            sleep(5)
            print("обучение закончено на 30%")
            sleep(5)
            print("обучение закончено на 40%")
            sleep(5)
            print("обучение закончено на 50%")
            sleep(5)
            print("обучение закончено на 60%")
            sleep(5)
            print("обучение закончено на 70%")
            sleep(5)
            print("обучение закончено на 80%")
            sleep(5)
            print("обучение закончено на 90%")
            sleep(5)
            print("обучение закончено на 99.9%")
            sleep(5)
            print("обучение закончено на 99.99%")
            sleep(5)
            print("обучение закончено на 100%") 
            sleep(randint(1,2))
            if 'ничего нету' in invent:
                invent.remove('ничего нету')
                rev = (f'образование учителя {tetche}')
                return rev
        else:
            print("обучение закончивается ... 0%")
            sleep(5)
            print("обучение закончено на 10%")
            sleep(5)
            print("обучение закончено на 20%")
            sleep(5)
            print("обучение закончено на 30%")
            sleep(5)
            print("обучение закончено на 40%")
            sleep(5)
            print("обучение закончено на 50%")
            sleep(5)
            print("обучение закончено на 60%")
            sleep(5)
            print("обучение закончено на 70%")
            sleep(5)
            print("обучение закончено на 80%")
            sleep(5)
            print("обучение закончено на 90%")
            sleep(5)
            print("обучение закончено на 99.9%")
            sleep(5)
            print("обучение закончено на 99.99%")
            sleep(5)
            print("обучение закончено на 100%") 
            sleep(randint(1,2))
            if 'ничего нету' in invent:
                invent.remove('ничего нету')
                rev = (f'образование учителя {tetche}')
                return rev
    
    else:
        print("обучение закончивается ... 0%")
        sleep(5)
        print("обучение закончено на 10%")
        sleep(5)
        print("обучение закончено на 20%")
        sleep(5)
        print("обучение закончено на 30%")
        sleep(5)
        print("обучение закончено на 40%")
        sleep(5)
        print("обучение закончено на 50%")
        sleep(5)
        print("обучение закончено на 60%")
        sleep(5)
        print("обучение закончено на 70%")
        sleep(5)
        print("обучение закончено на 80%")
        sleep(5)
        print("обучение закончено на 90%")
        sleep(5)
        print("обучение закончено на 99.9%")
        sleep(5)
        print("обучение закончено на 99.99%")
        sleep(5)
        print("обучение закончено на 100%") 
        sleep(randint(1,60))
        if 'ничего нету' in invent:
            invent.remove('ничего нету')
            rev =(f'образование {prower}') 
            return rev
