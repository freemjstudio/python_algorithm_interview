# 1043 거짓말 

n, m = map(int, input().split())
truth = list(map(int, input())) # 진실을 아는 사람의 수와 번호 
parents = [0]*(n+1)
for i in range(1, n+1):
    parents[i] = i # 부모를 자기 자신으로 초기화     

    
def find_parents(parents, x):
    if parents[x] != x:
        return find_parents(parents, parents[x])
    return parents[x]

def union(a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
        
result = 0 

if truth[0] == 0: # 진실을 아는 사람이 없을 때 
    result = 0 
else:
    # 진실을 아는 사람의 수 truth[0]
    for i in range(truth[0]):
        parents[truth[i]] = -1 # 진실을 아는 경우 -1을 부모로 설정
    
    for i in range(m):
        data = list(map(int, input().split()))
        for i in range(data[0]):
            now = data[i+1]
            if find_parents(parents, now):
                
        
        
print(result) # 최댓값 