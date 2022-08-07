# https://www.acmicpc.net/problem/11265

n, m = map(int, input().split()) # 파티장의 크기, 손님의 수 
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
for _ in range(m):
    start, end, cost = map(int, input().split()) 