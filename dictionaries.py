#Словарь состоит из ключей (строки, числа - что угодно) и значений (числа)
#Ключи не могут повторяться (иначе будет замена, см ниже)
#Словарь присваивается переменной

#d={'peter':12345, 'masha':85378, 'bob':1111}

#print (d['peter'])#напечатает значение 
#d['ann']=666666 #добавить значение
#d['bob']=222222 #изменили значение
#del d['bob'] #удалить значение

#Можно узнать длину словаря (число ключей):
#    len(d)

#Можно получить массив всех ключей или всех значений (в случайном порядке):
#    d.keys()
#    d.values()



#Распечатывает красиво:
#country={'ОАЭ': 'Абу-Даби',
#         'Бруней': 'Бандар-сери-Бегаван',
#         'Ямайка': 'Кингстон',
#         'Чили': 'Сан-Диего'}
#for key in country:
#    print(key, '-', country[key])


#Функция выдает столицу на запрос страны
#def countries(c):
#    country={'ОАЭ': 'Абу-Даби',
#             'Бруней': 'Бандар-сери-Бегаван',
#             'Ямайка': 'Кингстон',
#             'Чили': 'Сан-Диего'}
#    if c in country:
#        return(country[c])
#    else:
#        return(':(')
#
#print('Введите название страны:')
#print(countries(input()))


#Менять местами значения и ключи
#def revert():
#    country={'ОАЭ': 'Абу-Даби',
#             'Бруней': 'Бандар-сери-Бегаван',
#             'Ямайка': 'Кингстон',
#             'Чили': 'Сан-Диего'}
#    r_country={}
#    for key in country:
#        r_key=country[key]
#        r_country[r_key]=key
#    return(r_country)
#
#print(revert())


#Создать частотный список слов:
dictionary= {}
def open_file():
    wordlist=[]
    file = open('austen.txt', 'r', encoding='UTF-8')
    for line in file:
        linelist=line.split()
        for word in linelist:
            wordlist.append(word)
    file.close()
    return(wordlist)

def word_count(x):
    q=0
    for word in open_file():
        if word==x:
            q+=1
    return(q)

for word in open_file():
    quan=word_count(word)
    dictionary[word]=quan

for key in dictionary:
    print(key, dictionary[key])
