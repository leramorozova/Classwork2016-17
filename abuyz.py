quan=0
def func1(line):
    for i,word in enumerate(line):
        line=line.lower()
        line[i]=word.strip('.,?!;:')
    return line
file=open('C:/Users/student/Documents/Python Scripts/orwell.txt','r',encoding='utf8')
text=file.read()
for line in text:
    a=func1(line)
for word in line:
    quan+=1
print(quan)
    
