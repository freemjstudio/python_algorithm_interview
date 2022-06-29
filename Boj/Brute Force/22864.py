# 22864 피로도 

a, b, c, m = map(int, input().split())
state = 0 # 피로도 
task = 0 # 최대 일 할 수 있는 양 
if a > m:
    print(task)
else:
    for i in range(24): # 하루 24시간 
        if state+a <= m:
            state += a
            task += b
        else:
            if state-c >= 0: 
                state -= c
            else: # 피로도가 음수이면 0인걸로 친다 
                state = 0 
    
    print(task)
