# 9252

S1 = input()
S2 = input()

n = len(S1)
m = len(S2)

dp = [[""] * (m+1) for _ in range(n+1)] 


for i in range(1, n+1):
    for j in range(1, m+1):
        if S1[i-1] == S2[j-1]: # 같은 문자일 경우 
            dp[i][j] = dp[i-1][j-1] + S1[i-1]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
            
        
print(len(dp[-1][-1]))
print(dp[-1][-1])

