# 지구온난화 https://www.acmicpc.net/problem/5212
import copy 
r, c = map(int, input().split())
data = [] # X는 땅  . 는 바다
# . 세곳 or 네곳 인접하면 잠겨버린다 
for _ in range(r):
    data.append(list(input()))
result = copy.deepcopy(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 온난화 과정 
for x in range(r):
    for y in range(c):
        if data[x][y] == '.':
            continue
        cnt = 0 
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
    
            if nx < 0 or nx >= r or ny < 0 or ny > c:
                cnt += 1
                continue
            elif data[nx][ny] == '.':
                cnt += 1
        if cnt >= 3:
            result[x][y] = '.'

print("")
for i in range(r):
    for j in range(c):
        print(result[i][j],end='')
    print()           
# 지도 영역 체크하기 
start_row = 0 
end_row = 0 

start_col = c-1
end_col = 0 


# column 마지막 index 

for i in range(r):
    if 'X' in result[i]:
        start_row = i 
        break 
    
for i in range(r-1, -1, -1):
    if 'X' in result[i]:
        end_row = i 
        break 

for i in range(start_row, end_row+1):
    temp = [i for i, value in enumerate(result[i]) if value == 'X']
    # enumerate 로 X가 있는 index만 꺼냄 
    if not temp: # temp 가 비었을 때 
        continue
    min_temp = temp[0] # 0번째 index 
    max_temp = temp[-1] # 맨마지막 index 
    start_col = min(start_col, min_temp)
    end_col = max(end_col, max_temp)

print(start_col)
print(end_col)
for x in range(start_row, end_row+1):
    for y in range(start_col, end_col+1):
        print(result[x][y], end="")
    print()
        


        