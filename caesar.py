alpha='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print ('Encode or decode?')
todo=input()
print ('Offset?')
offset=int(input())
print ('Enter the data')
message=input()

result=''

for letter in message:
    if letter.lower() in alpha:
        num=alpha.index(letter.lower())
        if todo=='encode':
            newnum=(num+offset)%len(alpha)
        else:
            newnum=(num-offset)%len(alpha)
        if letter.isupper():
            result += alpha[newnum].upper()
        result +=alpha[newnum]
    else:
        result += letter
print(result)
