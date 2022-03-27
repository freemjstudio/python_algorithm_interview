# 1043 거짓말 

n, m = map(int, input().split())
truth = list(map(int, input().split())) # 진실을 아는 사람의 수와 번호 
truth_set = set(truth[1:])
party_list = []
result_list = [0]*(m)

for i in range(m):
    data = list(map(int, input().split()))
    party_list.append(set(data[1:]))
    result_list[i] = 1 # 1로 초기화한다. 

for _ in range(m):
    for i, party in enumerate(party_list):
        if truth_set.intersection(party): # 교집합이 있으면 0
            result_list[i] = 0
            truth_set = truth_set.union(party)
            

print(sum(result_list))