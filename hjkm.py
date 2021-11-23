key = str(input())
text = str(input())
text = text.replace(' ', '')
alf = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(text)):
    index = alf.find(text[i])
    sdvg = alf.find(key[i % (len(key))])
    index = (index + sdvg) % 26
    print(alf[index], end='')
