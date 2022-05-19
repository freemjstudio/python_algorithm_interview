# 1520 내리막 길  

m, n = map(int, input().split())
graph = []

for i in range(m):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[-1]*n for _ in range(m)]

# 방문되지 않았고, 현재 값보다 작은 숫자이면 이동할 수 있다 -> dfs()     
def dfs(x, y):
    
    if x == m-1 and y == n-1:
        return 1 # 경로 개수 1 
    
    if dp[x][y] != -1: # 방문한적 x, 경로 없음
        return dp[x][y] # 경로 개수 0 
    dp[x][y] = 0 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]
                    
            
print(dfs(0,0))