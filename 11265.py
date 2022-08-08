# https://www.acmicpc.net/problem/11265
# Floyd 
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 파티장의 크기, 손님의 수 
array = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if array[i][j] > array[i][k] + array[k][j]:
                array[i][j] = array[i][k] + array[k][j]
                    
for _ in range(m):
    start, end, cost = map(int, input().split()) 
    if array[start-1][end-1] <= cost:
        print("Enjoy other party")
    else:
        print("Stay here")