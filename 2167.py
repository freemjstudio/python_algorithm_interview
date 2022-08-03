# 2차원 배열의 합 https://www.acmicpc.net/problem/2167

N, M = map(int, input().split())
data = []
dp = [[0]*(M+1) for _ in range(N+1)]

for _ in range(N):
    data.append(list(map(int, input().split())))

# 누적합을 dp에 저장한다 
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + data[i-1][j-1]

T = int(input())

for _ in range(T):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
    