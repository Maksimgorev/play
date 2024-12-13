from random import randint
vrag = {    
'Америка' :{
    'военные':{
        'hp':100,
        'attak':(randint(1,10)),
        'deff':(randint(1,10))
    },
    'Моряки':{
        'hp':100,
        'attak':(randint(1,10)),
        'deff':(randint(1,10))
    },
    'танкисты ':{
        'hp':100,
        'attak':(randint(1,10)),
        'deff':(randint(1,10))  
    }
},
'''Украина''':{
    'военные':{
        'hp':100,
        'attak':(randint(1,10)),
        'deff':(randint(1,10))
    },
    "моряки":{
        'hp':100,
        'attak':(randint(1,10)),
        'deff':(randint(1,10))
    },
    "танкисты":{
        'hp':100,
        'attak':(randint(1,10)),
        'deff':(randint(1,10))
    }
}
}



plaer = {

    'Name' : input("напишите имя"),
    'hp' : 100,
    'здоровье': 1,
    'атака' : 1,
    'защита' : 1,
    'деньги' : 1000
    
}
voins ={    
    'военные':{
        'hp':100,
        'attak':(randint(1,10)),
        'deff':(randint(1,10))
    },
    "моряки":{
        'hp':100,
        'attak':(randint(1,10)),
        'deff':(randint(1,10))
    },
    "танкисты":{
        'hp':100,
        'attak':(randint(1,10)),
        'deff':(randint(1,10))
    }
}
max_level = 10
invent = ['ничего нету']

things = {
    'мечь':{
        'summa': 100,
        'strength':(randint(1,10)),
        'attak': 2
    },
    'пистолет':{
        'summa':500,
        'strength':(randint(1,10)),
        'attak': 3,
    },
    'автомат':{
        'summa':10000,
        'strength':(randint(1,10)),
        'attak': 4
    },
    'бронежелет':{
        'summa':100,
        'strength':( randint(1,10)),
        'deff':10 
    }
}

prowers = {
    "учитель":3.10,
    "таксист":2.30,
    "торговое дело":2.10,
    "сварщик":2.10,
    "автомеханик":2.10,
    "техника и искусство фотографии":2.10,
    "стагочный обработчик":2.10,
    "графический дизайн":3.10,
    "информационные системы и программирование":3.10,
    "дизайн среды (интерьер)":3.10
}