# 링크와 스타트 
from itertools import combinations

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

INF = int(1e9)
result = INF # 스타트와 링크 능력치 차이 
member = [i for i in range(n)]

for i in range(1, int(n/2)+1): # 1~ n//2 까지 확인하기 
    comb_team = combinations(member, i)
    min_diff = INF
    for comb in comb_team: # 조합을 하나씩 조회하기 
        start = list(comb) # comb 는 set를 반환하므로 list로 바꿔주어야 함 
        link = list(set(member)-set(start))
        start_sum = 0 
        link_sum = 0 
        for x in range(n-1): # start & link는 최대 팀원수가 n-1 명이므로 ~ 인덱스조회
            for y in range(n-1):
                try:
                    s = data[start[x]][start[y]]
                except IndexError:
                    s = 0 
                try:
                    l = data[link[x]][link[y]]
                except IndexError:
                    l = 0 
                start_sum += s
                link_sum += l
    
        diff = abs(start_sum - link_sum)
        min_diff = min(diff, min_diff)
    result = min(min_diff, result)

print(result)