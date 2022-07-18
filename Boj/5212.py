# 지구온난화 https://www.acmicpc.net/problem/5212
import copy 
r, c = map(int, input().split())
data = [] # X는 땅  . 는 바다
result = copy.deepcopy(data)
# . 세곳 or 네곳 인접하면 잠겨버린다 
for _ in range():
    line = list(map(int, input().split()))
    data.append(list)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(r):
    for y in range(c):
        if data[x][y] == 'X':
            cnt = 0 
            for k in range(4):
                x = dx[k] + x
                y = dx[k] + y
                if data[x][y] == '.':
                    cnt += 1
            if cnt >= 3:
                result[x][y] = '.'
                
# 출력할 때 ? . 만 테두리 있으면 삭제하기 
for x in range(r):
    for y in range(c):
        if result[x][y]         
        