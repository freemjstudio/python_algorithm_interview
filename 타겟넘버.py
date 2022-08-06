from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    
    queue.append((numbers[0], 0))
    queue.append((-1)*(numbers[0], 0))
    
    while queue:
        
    
    return answer