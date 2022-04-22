n = 5 # 데이터의 개수 
m = 5 # 찾고자 하는 부분합 M
data = [i for i in range(1, n+1)]
count = 0 
interval_sum = 0 
end = 0 

for start in range(n):
    # end 만큼 이동시키기 
    while interval_sum < m and end <n:
        interval_sum += data[end]