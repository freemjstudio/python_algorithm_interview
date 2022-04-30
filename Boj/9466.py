# 9466 
import sys
sys.setrecursionlimit(999999)

def dfs(x):
    global result
    visited[x] = True 
    cycle.append(x)
    
    if visited[data[x]]: # True 
        if data[x] in cycle:
            result += cycle[cycle.index(data[x]):]
    else: # False 
        dfs(data[x])
    
t = int(input())   
for _ in range(t):
    n = int(input()) # 학생수 
    data = [0] + list(map(int, input().split()))
    visited = [False]*(n+1)
    result = []
    
    for i in range(1, n+1):
        if visited[i] == False:
            cycle = [] 
            dfs(i)
    print(n-len(result))
            
    
    

    
