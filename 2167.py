# 2차원 배열의 합 https://www.acmicpc.net/problem/2167

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

T = int(input())
for _ in range(T):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    x -= 1
    y -= 1
    sum = 0 
    for i in range(a, x+1):
        for j in range(b, y+1):
            sum += data[i][j]
    print(sum)
    