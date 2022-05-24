# 2573 빙산 
# 맞닿아 있는 변의 개수만큼 -n 된다. 

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # 상하좌우 이동 
