# https://www.acmicpc.net/problem/1325
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a) # 방향성이 있는 그래프 


result = []

for i in range(len(result)):
    print(result[i], end=' ')
