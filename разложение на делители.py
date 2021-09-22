num = int(input()) #75
for i in range (1, int((num**0.5)+1)):
    if num % i == 0:
        print(i, num//i)
    i += 1
