# 1043 거짓말 

n, m = map(int, input().split())
truth = list(map(int, input())) # 진실을 아는 사람의 수와 번호 
truth_set = truth[1:] 
result = 0 

if truth[0] == 0: # 진실을 아는 사람이 없을 때 
    result = 0 
else:
    # 진실을 아는 사람의 수 truth[0]
    for i in range(m):
        data = map(int, input())
        result += 1
        for i in data[1:]:
            if i in truth_set:
                result -= 1
                break 
            
        
print(result)