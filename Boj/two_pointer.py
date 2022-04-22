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
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start] # start 포인터를 이동시키므로 이전 값은 빼주어야 한다. 

print(count)