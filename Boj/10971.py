# 10971 외판원 순회 2 
INF = int(1e9)

n = int(input())
weight = []
min_total_weight = INF 

for i in range(n):
    weight.append(list(map(int, input().split())))

def dfs(visited, now, next, value): # value : 현재까지의 sum 
    global min_total_weight # sum of the weight 
    
    if len(visited) == n:
        if weight[next][now] != 0: # 출발점으로 되돌아가는 경로가 있다면 
            min_total_weight = min(min_total_weight, value + weight[next][now])
        return 
    for i in range(n):
        if weight[next][i] != 0 and i not in visited and value < min_total_weight:
                visited.append(i)
                dfs(visited, now, i, weight[next][i] + value)
                visited.pop()
                
# 각 도시를 출발점으로 고려한다 
for i in range(n):
    dfs([i], i, i, 0)

print(min_total_weight)
     