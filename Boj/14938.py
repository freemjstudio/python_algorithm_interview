# 서강그라운드 14938
# 플로이드 워셜 알고리즘으로 모든 경로의 최소거리를 계산 
INF = int(1e9)
n, m, r = map(int, input().split()) # 지역의 개수, 수색범위, 길의 개수 
item = list(map(int, input().split())) # 아이템의 수 
graph = [[INF]*n for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split()) # 길 양끝에 존재하는 지역의 번호, 길이
    graph[a-1][b-1] = min(graph[a-1][b-1], l)
    graph[b-1][a-1] = min(graph[b-1][a-1], l)
    
max_item = 0 #최대 구할 수 있는 아이템 개수 

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            if i == j:
                graph[i][j] = 0 # 자기 자신 

for i in range(n):
    temp_item = 0 
    for j in range(n):
        if graph[i][j] <= m: # 수색 범위 이하인지 체크하기 
            temp_item += item[j] 
    max_item = max(temp_item, max_item)

print(max_item)