# https://www.acmicpc.net/problem/11000
# 강의실 배정 
import heapq # 우선순위 큐 라이브러리 사용하기 

n = int(input())
times = []

for _ in range(n):
    s, t = map(int, input().split()) 
    times.append((s, t))

times.sort() # s 를 기준으로 정렬한다 
room = [] # priority queue 
heapq.heappush(room, times[0][1]) # 첫 회의 종료시간을 넣는다 

for i in range(1, n):
    if times[i][0] > room[0]: # 두번째 회의 시간이 첫 회의 시간보다 더 느린 경우 -> 룸 개수 추가 안됨 
        heapq.heappop(room)
        heapq.heappush(room, times[i][1])
    else:
        heapq.heappush(room, times[i][1])
        
print(len(room))