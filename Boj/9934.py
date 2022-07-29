# 완전 이진 트리 https://www.acmicpc.net/problem/9934

k = int(input())
data = list(map(int, input().split())) 
tree = [[] for _ in range(k)] # 층 수별 트리 

def make_tree(array, x):
    mid = len(array)//2
    tree[x].append(array[mid])
    if len(array) == 1:
        return 
    make_tree(array[:mid], x+1) # level 한단계 추가시키기 
    make_tree(array[mid+1:], x+1) 

make_tree(data, 0)

for i in range(k):
    print(*tree) 