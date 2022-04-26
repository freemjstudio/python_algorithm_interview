# 팰린드롬?
from collections import deque

n = int(input())
data = [0]+list(map(int, input().split()))
m = int(input())

def check(s, e): # 펠린드롬 확인 
    queue = deque(data[s:e+1])
    
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True 

for _ in range(m):
    s, e = map(int, input().split())
    if check(s, e):
        print(1)
    else:
        print(0)
    

    
    
    