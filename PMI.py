import re
import os
from math import log

punct = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]'

def preprocessing(text): #удаляем все знаки пунктуации и возвращаем массив слов
                         #в нижнем регистре
    long_words=[]
    text_wo_punct = re.sub(punct, '', text.lower())
    words = text_wo_punct.strip().split()
    for word in words:
        if len(word)>4:
            long_words.append(word)
    return long_words

#составляем частотный список слов
with open('news.txt', 'r', encoding='utf-8') as f:
    long_words = preprocessing(f.read())

word_freq = {}
for word in long_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

#составляем частотный список биграмм (просто собираем все пары слов)
bigrams = []
for ind in range(1, len(long_words) - 1):
    bigrams.append(' '.join([long_words[ind - 1], long_words[ind]]))
    
bigram_freq = {}
for b in bigrams:
    if b in bigram_freq:
        bigram_freq[b] += 1
    else:
        bigram_freq[b] = 1

#считаем пми
def count_pmi(x, y):
    p_xy = bigram_freq[' '.join([x, y])]/len(bigram_freq)
    p_x, p_y = word_freq[x]/len(word_freq), word_freq[y]/len(word_freq)
    pmi = log(p_xy/(p_x * p_y))
    return pmi

#создаемеще словарь для биграмм+пми
pmi = {}
for bigr in bigrams:
    x, y = bigr.split()
    pmi[bigr] = count_pmi(x, y)

i = 0
#for bigram in sorted(pmi, key = lambda m: -pmi[m]):#если убрать -, то будут последние биграммы
#сортед - оператор, который сортирует заданные списки. Всегда возвращает массив
#если в первую позицию поставить словарь, он берет ключи и сортирует их
#в key нужно писать функцию по чему мы сортируем (лен - будет по длине)
#ламбда - анонимная функция, функция у кот нет имени
#c помощью этой замороченной строки сортировка ключей идет по значениям, а не ключам
#    if i > 100:
#        break
#    print(bigram, pmi[bigram])
#    i += 1




#считаем, насколько часто биграммы встречаются в разных категориях текстов
anek = ''
teh = ''
izvest = ''
for root, dirs, files in os.walk('texts'):
    for f in files:
        if 'anekdots' in root:
            num_anek = len(files)
            anek += open(os.path.join(root, f), encoding='utf-8').read()
        elif 'izvest' in root:
            num_izvest = len(files)
            izvest += open(os.path.join(root, f), encoding='utf-8').read()
        elif 'teh_mol' in root:
            num_teh = len(files)
            teh += open(os.path.join(root, f), encoding='utf-8').read()
            
words_anek = preprocessing(anek)
words_teh = preprocessing(teh)
words_izvest = preprocessing(izvest)

words = words_anek + words_teh + words_izvest


def freq_dict(arr):
    dic = {}
    for element in arr:
        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1
    return dic

def bfreq_creator(text):
    bigrams = []
    for ind in range(1, len(text) - 1):
        bigrams.append(' '.join([text[ind - 1], text[ind]]))
    bigram_freq = {}
    for b in bigrams:
        if b in bigram_freq:
            bigram_freq[b] += 1
        else:
            bigram_freq[b] = 1
    return bigram_freq

print(bfreq_creator(words_anek))
b_creator(words_teh)
b_creator(words_izvest)


corpus_freq = freq_dict(words)
anek_freq = freq_dict(words_anek)
izvest_freq = freq_dict(words_izvest)
teh_freq = freq_dict(words_teh)

#х - это слово, у - это категория
def pmi_for_cats(x, y):
    if y == 'anek':
        dic = anek_freq
        num = num_anek
    elif y == 'teh':
        dic = teh_freq
        num = num_teh
    elif y == 'izvest':
        dic = izvest_freq
        num = num_izvest
    p_xy = dic[x]/len(dic)
    p_x, p_y = corpus_freq[x]/len(corpus_freq), num/(num_izvest + num_teh + num_anek)
    pmi = log(p_xy/(p_x * p_y))
    return pmi

cat_pmi = {}
i = 0
#for word in corpus_freq:
#    if i > 100:
#        break
#    try:
#        pmi_anek = pmi_for_cats(word, 'anek')
#    except KeyError:
#        pmi_anek = 0
#    try:
#        pmi_teh = pmi_for_cats(word, 'teh')
#    except KeyError:
#        pmi_teh = 0
#    try:
#        pmi_izvest = pmi_for_cats(word, 'izvest')
#    except KeyError:
#        pmi_izvest = 0
#    max_pmi = max(pmi_anek, pmi_teh, pmi_izvest)
#    if max_pmi == 0:
#        continue
#    if max_pmi == pmi_anek:
#        cat = 'anek'
#    elif max_pmi == pmi_teh:
#        cat = 'teh'
#    elif max_pmi == pmi_izvest:
#        cat = 'izvest'
#    print(word, cat)
#    i += 1

