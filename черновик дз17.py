import os

dirlist=[el for root, dirs, files in os.walk('.') for el in dirs]

stat={}

letters='qwertyuiopasdfghjklzxcvbnm��������������������������������'

letter=[name[0].lower() for name in dirlist]

for el in letter:
    if el not in letters:
        letter.remove(el)

print (letter)

for el in letter:
    if el in stat:
        stat[el]+=1
    else:
        stat[el]=1

i=0
res=0
for value in stat:
    if stat[value]>i:
        i=stat[value]
        res=value

#print('���� ����� �������� ���������� �:', res, '\n����� � ����� ��������� �����������', i, '���')
    
