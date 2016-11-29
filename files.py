#f=open('file.format(или путь)','r(read)/w(write)/i(добавить в конец)')
#encoding='utf-8' (ANSI, cp1251)
#text=f.read()
#print(text)
#f.close()

#\n - перенос строки

#Читаем файл
#f=open('C:/Users/student/Documents/Python Scripts/orwell.txt', 'r', encoding='utf-8')
#text=f.read()
#print(text) - выведет текст/print(len(text)) - выведет число символов
#f.close()

#Создаем файл и пишем в нем
#f=open('C:\\Users\\student\\Documents\\Python Scripts\\new.txt','w',encoding='utf-8')
#text=f.write('privet')
#f.close()

#Печатаем по строкам
#f=open('C:/Users/student/Documents/Python Scripts/orwell.txt', 'r', encoding='utf-8')
#for line in f:
#    print('начало строки', line, 'конец строки')
#f.close()

#s='a, b, c, d, e, f'
#arr=s.split(', ') - если разделителей нет, оставить скобки пустыми
#print(arr)


#Считаем кол-во слов
#f=open('C:/Users/student/Documents/Python Scripts/orwell.txt', 'r', encoding='utf-8')
#quan=0
#for line in f:
#    arr=line.split()
#    for word in arr:
#        arr2=word.split()
#        quan+=1
#print(quan)

#Печатаем кажду. вторую строку
#f=open('C:/Users/student/Documents/Python Scripts/orwell.txt', 'r', encoding='utf-8')
#quan=1
#arr=[]
#for line in f:
#    arr2=line.split()
#    if quan%2==0:
#        print (line)
#    quan+=1
#f.close()


f=open('C:/Users/student/Documents/Python Scripts/new.txt', 'r', encoding='utf-8')
quan=0
quan2=0
mas=[]
for line in f:
    arr=line.split()
    for word in arr:
        arr2=word.split()
        quan+=1
        if word not in mas:
            mas.append(word)
            quan2+=1
        else:
            continue
print(quan,'разных слов:',quan2)
f.close()
