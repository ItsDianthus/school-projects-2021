num = int(input()) #18 = 2 3 3
i = 2
while num > 0:
    if num % i == 0:
        print(i)
        num //= i # 9
    else:
        i += 1 # 3

    
