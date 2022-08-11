#21608 상어초등학교 

n = int(input())
seat_array = [] # 자리 배치 
result = 0 # 만족도의 총합 구하기 
student_dict = {} # dictionary 
# 입력받기 
for i in range(n*n):
    data = list(map(int, input().split()))
    student = data[0]
    student_dict[student] = data[1:]
    
    
    