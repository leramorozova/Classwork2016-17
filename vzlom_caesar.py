alpha='abcdefghigklmnopqrstuvwxyz'
message='Drsc zkbbyd sc xy wybo. Sd rkc mokcon dy lo.'
for offset in range(len(alpha)):
    result=''
    for letter in message:
        if letter.lower() in alpha:
            num=alpha.index(letter.lower())
            newnum=(num-offset)%len(alpha)
            if letter.isupper():
                result+= alpha[newnum].upper()
            else: result += alpha[newnum]
        else:
            result +=letter
    print(offset, '-', result)
    
