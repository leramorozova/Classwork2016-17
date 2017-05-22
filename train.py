import os


f=open('table.csv', 'r', encoding='utf-8')

stro=({},{},{})

for root, dirs, files in os.walk('wikipedia'):
    stro.format(files, os.listdir(files), 4)
