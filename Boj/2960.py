# 2960 에라토스테네스의 체 

from re import T


n, k = map(int,input().split())
count = 1

numbers = [True for _ in range(n+1)]
numbers[2] = False 
p = 2 # 첫번째 p , 가장 작은 소수: 2
now = p
while True:
    if count == k:
        break
    for i in range(p+1, n+1):
        if i%p == 0 and numbers[i] == True:
            numbers[i] = False
            count += 1
            now = i

print(now)
    