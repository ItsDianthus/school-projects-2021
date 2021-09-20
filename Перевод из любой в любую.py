# вводятся три числа: а, его система счисления, система в которую
# переводится число.  На выходе число в х СС
a = str(input())
base1 = int(input())
base2 = int(input())
num10 = 0
fin = ''
alf = '0123456789ABCDEF'
if base1 != 10:
    for i in range(len(a)):
      num10 = int(alf.find(a[i])) * base1 ** (len(a) - 1 - i) + num10
else:
    num10 = a
if base2 == 10:
    print(num10)
else:
    num10 = int(num10)
    while num10 > 0:
        fin = alf[int(num10)%base2] + str(fin)
        num10 //= base2
    print(fin)
