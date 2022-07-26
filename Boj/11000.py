# https://www.acmicpc.net/problem/11000
# 강의실 배정 
import heapq # 우선순위 큐 라이브러리 사용하기 

n = int(input())
count = 0 # 강의실의 개수 
times = []

for _ in range(n):
    s, t = map(int, input().split()) 
    times.append((s, t))

times.sort() 
