# 2015 수들의 합 4
from collections import defaultdict

n, k = map(int, input().split())
array = list(map(int, input().split()))

totalsum = defaultdict(int)
count = 0 

for i in range(1, n):
    array[i] += array[i-1]

for i in range(n):
    if array[i] == k: # 누적합 체크 
        count += 1
    count += totalsum[array[i]-k] # S[i-1] == S[i] - k 이면 1 더해지고 아니면 0임 
    totalsum[array[i]] += 1 # 누적합이 S[i] 이 되는 경우 (딕셔너리 값을 올려준다)
    
print(count)

