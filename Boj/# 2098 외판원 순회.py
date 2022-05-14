# 2098 외판원 순회 

n = int(input()) # 0 ~ n-1 
weight = [] # 비용 
dp = []
for i in range(n):
    for j in range(n):
        weight.append(list(map(int, input().split())))



print(min(dp))