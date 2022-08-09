# https://www.acmicpc.net/problem/1325
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a) # 방향성이 있는 그래프 

def bfs(start): # start node 
    count = 0 
    visited = [False for _ in range(n+1)]
    visited[start] = True 
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if visited[now] == False:
            queue.append(now)
            visited[now] = True
            count += 1
    return count 

result = []
max_count = 0
for i in range(1, n+1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        result.append(i)
    
result.sort() # 오름차순 정렬하기 
for i in range(len(result)):
    print(result[i], end=' ')
