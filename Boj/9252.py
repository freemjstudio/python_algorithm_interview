# 9252

S1 = input()
S2 = input()

n = len(S1)
m = len(S2)

dp = [[0] * (m+1) for _ in range(n+1)] # length of the LCS
dp2 = [[]*(m+1) for _ in range(n+1)] # alphabet dp 


for i in range(1, n+1):
    for j in range(1, m+1):
        if S1[i-1] == S2[j-1]: # 같은 문자일 경우 
            dp[i][j] = dp[i-1][j-1] + 1
            dp2[i][j].append(dp[i-1][j-1])
            dp2[i][j].append(S1[i-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if dp[i-1][j] > dp[i][j-1]:
                dp2[i][j].append(dp2[i-1][j])
            else:
                dp2[i][j].append(dp2[i][j-1])
            
        
print(dp[-1][-1])
print(''.join(dp2[-1][-1]))

