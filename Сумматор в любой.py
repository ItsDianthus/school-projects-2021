a = int(input())
b = int(input())
base = int(input())
rem = 0
fin = ''
while a > 0 or b > 0:
    summ = a % 10 + b % 10 + rem
    if summ > 1:
        rem = summ // base
        fin = str(summ % base) + fin
    b //= 10
    a //= 10
if rem != 0:
     print(str(rem) + fin)
else:
    print(fin)
    
    
    
