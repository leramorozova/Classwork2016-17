-----List comprehensions-----

a=[1,2,3,4,5,6]
b=[]
for i in a:
    b.append(i**2)

OR

new_b=[i**2 for i in a]
new_b=[i**2 for i in a if i%2==0] - можно вписать в условие

words=['Mary', 'Jane', 'Shawn']
words+=['Tom'] - можно добавить слово
new_words = [w.upper() for w in words]
new_words = [w.upper() for w in words if 'J' in w or 'j' in w]
new_words2 = [w.upper() for w in words if re.search('[JjAa]', w)]

BIG_ARR=[a,b,new_b,words] - массив массивов
for arr in BIG_ARR:
    for item in arr:
        flat.append(item)

OR

flat=[item for arr in BIG_ARR for item in arr] - на выходе будет один большой
массив с элементами из всех массивов


-----Dict comprehensions------
    
a=[1,2,3,4,5,6]
squared={i: i**2 for i in a} - до двоеточия - ключ, после - значение
animals={'собака':'гав','кошка':'мяу','утка':'кря'}
sounds={animals[animal]: animal for animal in animals} - поменяли местами ключ
и значение
sounds={animals[animal]: animal for animal in animals if len(animal)>4} - отсекает
названия животных, если они короче 4

-----Format (форматирование строк)-----
s.upper()
s.lower()
s.capitalize()
s.title()

s='Hello,{}!'
s2='Harry'
s.format(s2) => 'Hello, Harry!' - позволяет создавать шаблон
s.format(s2).upper => 'HELLO, HARRY!'

ex='Name: (), surname: (), age ()'
ex.format('Tom', 'Smith', '34') => 'Name: Tom, surname: Smith, age 34'
цифры можно не писать как строки (можно без скобок). На месте строк в формате
могут быть переменные

h = 'Вас зовут {0} {1}. Зовут вас {1} {0}.'.format('Петя','Иванов')
Вас зовут Петя Иванов. Зовут вас Иванов Петя.

template= 'Age: {:>4}'
ages=[1,2,34,100]
for age in ages:
    print(template.format(age))
Получится с выравниванием
> выравнивание влево
< выравнивание вправо (по умолчанию)
^ выравнивание по центру
число после этого символа - число символов дальше
:+>10 (длина строки 10, пустота заполнится +

'Shablon: {:.5}'.format('texttexttext') - входная строка обрежется до 5 символов
'Shablon: {:10.5}'.format('texttexttext') - длина строки 10, но входная обрезается
       до 5 символов
       {:2f} - округление десятичной дроби до 2х знаков после запятой
       
    


