#Программа должна просмотреть все папки и файлы, находящиеся
#в одной папке с ней, и сообщить, сколько найдено файлов,
#название которых состоит только из пяти латинских символов.
#Кроме этого, программа должна выводить на экран названия всех
#файлов или папок, которые она нашла, без повторов.

import os
import re

i=0
files=os.listdir()
name_base=[]

for item in files:
    file_name=item.split('.')
    if len(file_name[0])==5:
        lat=re.search('[A-Za-z]{5}', file_name[0])
        if lat!=None:
            i+=1
    if file_name[0] not in name_base:
        name_base.append(file_name[0])

print ('Число файлов с названием из пяти латинских символов: ',i)
print ('\nСписок названий найденных файлов (без повторов):')
for el in name_base:
    print (el)
