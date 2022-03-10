# 2740 행렬 곱셈 
# N*M , M*K 행렬을 곱하면 N*K 행렬이 된다. 

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]
result = [[0]*k for _ in range(n)]

for row in range(n):
    for col in range(k):
        e = 0 
        for i in range(m):
            e += A[row][i] * B[i][col]
        result[row][col] =  e
    
for i in result:
    print(*i)
