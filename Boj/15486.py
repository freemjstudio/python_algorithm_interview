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
    result = max(result, dp[i])
    if i+t[i] > n: # 주어진 일 수보다 긴 경우 -> 상담 불가능 
        continue
    dp[i+t[i]] = max(p[i]+result, dp[i+t[i]])
    

print(max(dp))