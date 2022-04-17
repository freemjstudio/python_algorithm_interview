# 소인수 분해 
n = int(input())

div = 2
while True:
    if n == 1:
        break 
    if n % div == 0:
        n = n/div
        print(div)
    else:
        div += 1
        