IMPORT OS

print(os.path.join('folder', 'file.txt')) - вернет путь от папки к файлу,
написанный по стандардам данной ОС.
os.listdir() - выводит имена всех файлов в папке
print(os.listdir(folder)) => ['1.txt', '2.txt', '4.txt', '3.txt']

folder = 'texts'
print(os.listdir(folder))
for f in os.listdir(folder):
     with open(os.path.join(folder, f)) as text:
        print('file: ', f, '   text: ', text.read())
['1.txt', '2.txt', '4.txt', '3.txt']
Output:
file:  1.txt    text:  1
file:  2.txt    text:  2
file:  4.txt    text:  4
file:  3.txt    text:  3

os.listdir('.') - показывает файлы в текущей папке
os.path.abspath('.') - покажет абсолютный путь к текущей папке

os.mkdir('new_folder') - создает новую папку с названием new_folder

os.path.exists('new_folder') - проверяет, существует ли папка с таким названием
внутри текущей (возвразает True или False)

Если папки не существует, можно тут же её и создать:
if not os.path.exists('new_folder2'):
    os.mkdir('new_folder2')

Возможно также создавать не одну папку, а целых несколько вместе, если
нам нужны вложенные друг в друга папки. Для этого используется функция
os.makedirs().
path = 'a/long/long/long/path'
os.makedirs(path)

os.rename(путь к файлу со старым названием, путь к файлу с новым)
- переименовать файл

Можно узнавать, заданный путь - это путь к папке или файлу?
Для этого используются функции os.isdir() и os.isfile().
Они принимают на вход путь, а возвращают True или False.
# texts - это папка?
os.path.isdir('texts')
Out: True

# А new_texts - то файл?
os.path.isfile('new_texts')
Out: False

os.rmdir() - удаление только пустых папок




IMPORT SHUTIL

shutul.copy(источник, точка назначения) - копировать файлы
shutil.move(источник, точка назначения) - перемещать файлы
Если файлы в точке назначения уже есть, будет ошибка

shutil.rmtree() - удаление не пустой папки

# Удалим файлы в папке texts
for f in os.listdir('texts'):
    if os.path.isfile(f):
        os.remove(os.path.join('texts'), f)

# а теперь удалим все папки, которые мы насоздавали в процессе работы
for f in os.listdir():
    if os.path.isdir(f):
        shutil.rmtree(f)
