#21608 상어초등학교 

n = int(input())
seat_array = [[0]*n for _ in range(n)] # 자리 배치 
result = 0 # 만족도의 총합 구하기 
student_dict = {} # dictionary -> 만족도 계산할 때 필요함 
# 입력받기 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for index in range(n*n):
    data = list(map(int, input().split()))
    student = data[0]
    student_dict[student] = data[1:]
    
    if index == 0:
        mid = (n//2)
        # 가운데에 배치하기 
        seat_array[mid][mid] = student
    else: # 첫번째 입력이 아닌 경우 
        temp = [] # 자리 후보
        # 좋아하는 학생 탐색 
        for x in range(n):
            for y in range(n):
                if seat_array[x][y] in student_dict[student]:
                    # temp.append((x,y))
                    # (x,y) 상하좌우로 빈자리인지 확인하기 
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        
                    
        
        
        # 조건 2번
        # 조건 3번 
    
    
    
    