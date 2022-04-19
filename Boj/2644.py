from collections import deque


n = int(input())
graph = [[] for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
a, b = map(int, input().split()) # 촌수를 계산해야 하는 두 사람
m = int(input()) # edges case
for _ in range(m):
    x, y = map(int, input().split()) # 부모 - 자식 
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    q = deque()
    q.append(start)
    visited = [False]*(n+1)
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == False:
                visited[i] = True
                distance[i] = distance[now] + 1
                q.append(i)
bfs(a)
if distance[b] != 0:
    print(distance[b])
else:
    print(-1)