# 2960 에라토스테네스의 체 

n, k = map(int,input().split())
count = 0
numbers = [True for _ in range(n+1)]
for i in range(2, n+1):
    if numbers[i] == True:
        for j in range(i, n+1, i):
            if numbers[j] == True: # 아직 지우지 않은 수이면
                numbers[j] = False # 지운다 
                count += 1 # 몇번째 지워진 수 인지 확인한다
            if count == k: # k 번째 지워진 수라면 답 출력 
                print(j)
                break 
            

    