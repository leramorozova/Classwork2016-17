#Пользователь вводит предложение на английском языке, и программа
#создает вложенные друг в друга папки, так чтобы путь к самой глубокой
#из них составлял введенное предложение. Например, если пользователь
#ввел предложение "It is a wonderful day", программа должна создать вложенные
#папки, и путь к последней из них должен быть "it/is/a/wonderful/day"

#import os

#print('Enter a phrase:')
#phrase = input()
#words=phrase.split()
#path='/'.join(words)
#os.makedirs(path)
#print('done')


#Пользователь вводит число, например, 3. Нужно создать количество папок в
#соответствии с введенным числом. В нашем случае это три папки, которые должны
#называться "1", "2", "3". В первой папке нужно создать один текстовый файл, во
#второй два файла, в третьей - три файла и т.д.

import os


num = int(input('Введите число: '))    
    for i in range(num):        
        dirname = str(i+1)        
        if not os.path.exists(dirname):            
            os.mkdir(dirname)            
            t = 'file{}.txt'            
            for fnum in range(1, i+1):                
                fname = os.path.join(dirname, t.format(fnum))                
                with open(fname, 'w', encoding='utf-8') as f:                    
                    f.write('..')

print ('done')
