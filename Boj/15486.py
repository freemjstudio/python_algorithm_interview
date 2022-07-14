# 15486

n = int(input())

t = [] # task 
p = [] # price 
dp = [0] * (n+1) # 해당일까지의 최대 이익을 저장 

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

result = 0 

for i in range(n): # 0 ~ n-1
    result = max()
    

print(max(dp))