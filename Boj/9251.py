# 9251 LCS 

import sys
S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()

a = len(S1)
b = len(S2)

dp = [[0]*(a+1) for _ in range(b+1)]

for i in range(1, a+1):
    for j in range(1, b+1):
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) 
            
print(dp[-1][-1]) # 맨 마지막 원소 

            