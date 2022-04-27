# 팰린드롬?
# DP 로 풀이 

n = int(input())
data = list(map(int, input().split()))
m = int(input())
dp = [[0]* n for _ in range(n)] # n*n dp table 

for start in range(n):
    for j in range(n-start):
        end = start + j 
        if end == start:
            dp[start][end] = 1
        elif data[start] == data[end]: # 시작점과 끝점이 동일하면
            if end - start == 1: # 문자열 길이가 2라면 펠린드롬
                dp[start][end] = 1 
            elif dp[start+1][end-1] == 1: # 가운데 문자열이 펠린드롬이면 펠린드롬
                dp[start][end] = 1
        

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
    

