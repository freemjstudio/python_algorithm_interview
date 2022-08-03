# 2015 수들의 합 4

n, k = map(int, input().split())
array = list(map(int, input().split()))

# A[1], A[2] ... A[N]

# 합이 k 인 부분합의 개수 
dp = [[0]*n for _ in range(n)]

count = 0 

for i in range(n):
    for j in range(i, n):
        if i == j:
            dp[i][j] = array[i]
        if i < j:
            dp[i][j] = dp[i][j-1] + array[i]
        
for i in range(n):
    for j in range(n):
        if dp[i][j] == k:
            count += 1
            
print(count)
