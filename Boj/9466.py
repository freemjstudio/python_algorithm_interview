# 9466 텀 프로젝트 

t = int(input())
    
def dfs(x):
    global team 
    visited[x] = True
    cycle.append(x) # 맨 처음 팀원
    
    if visited[data[x]]: # 이미 방문했다면 사이클 여부를 확인한다 
        if data[x] in cycle:
            team += cycle[cycle.index(data[x]):] # cycle이 되는 구간이 팀을 이룸
        return 
    else: # 아직 방문하지 않은 데이터라면 다시 dfs로 순환한다. 
        dfs(data[x]) # 아직 방문안했으면 
    
    
    

for _ in range(t):
    n = int(input())
    visited = [False]*(n+1)
    data = [0] + list(map(int, input().split())) 
    team = []
    
    for i in range(1, n+1):
        if visited[i] == False:
            cycle = []
            dfs(i)
    
    #result 
    print(n - len(team))
    

    
