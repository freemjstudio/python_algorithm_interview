# https://www.acmicpc.net/problem/20436 zoac3
import itertools

left, right = input().split()
word = input()
# 택시거리를 구하기 
keyboard = ['qwertyuiop',
            'asdfghjkl',
            'zxcvbnm']

x1, y1 = -1, -1 # a 좌표 
x2, y2 = -1, -1 # b 좌표 

# keyboard row 에 있는지 검사 -> column 에서 index() 함수 써서 위치 반환하기 
for i in range(len(word)):
    
    
    
diff = abs(x1-x2) + abs(y1-y2) # 걸리는 시간 
