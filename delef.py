from day_Shop import *
import delif1
from time import sleep

adc =('''
Разработчик игры максим горев 
Хочу сказать пару слов о Easycode хорошая школа очень рад в ней учиться 
о игре хотелось сказать что игра была легкой но проблемы тоже были что я написал не так и пытался не дождаться ошибки 
бывало что код удалял но потом снгва сидел и востанавливал то что хотел написать 
самые  лучшие учителя это
Владислав Гребенщиков
Артур Сидоров который провел одно занятие с со мной и объяснил как работат функции 'global' и 'return'
''')

def exik():
    print("досвидание ")
    sleep(10)
    return ("вы вышли из игры")

def timeslepper():
    yes_no1 = input("хотите  прокачаться?")
    if yes_no1 == "да":
        h_a_d = input("что хотите")
        if max_level > plaer[h_a_d]:
            spid = input("хотите быстро прокачаться?")
            if spid == "нет":
                print("качается уровень ... 0%")
                sleep(5)
                print("качается уровень 10%")
                sleep(5)
                print("качается уровень 20%")
                sleep(5)
                print("качается уровень 30%")
                sleep(5)
                print("качается уровень 40%")
                sleep(5)
                print("качается уровень 50%")
                sleep(5)
                print("качается уровень 60%")
                sleep(5)
                print("качается уровень 70%")
                sleep(5)
                print("качается уровень 80%")
                sleep(5)
                print("качается уровень 90%")
                sleep(5)
                print("качается уровень 99.9%")
                sleep(5)
                print("качается уровень 99.99%")
                sleep(5)
                print("качается уровень 100%")
                level = plaer[h_a_d]
                nev_level = plaer[h_a_d]
                nev_level1 = nev_level + 1
                plaer[h_a_d] = nev_level1
                return nev_level1

            else:
                print("качается уровень 100%")
                level = plaer[h_a_d]
                nev_level = plaer[h_a_d]
                nev_level1 = nev_level + 1
                plaer[h_a_d] = nev_level1
                return nev_level1


def bolnica():
    what = input('''
    что вы хотите от больницы''')
    if what == 'получить справки' or 'справки':
        what1 = input('какую вы хотите справку')
        print('''
        от здоровья
        от психики
        ''')
        a = input ()
        if a == 'от психики' or '2':
            print(delif1.psix())
        else:
            print(delif1.hped())

    elif what == 'вылечиться':
        delif1.hped()