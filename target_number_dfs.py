def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(temp, index):
        if index == n:
            if temp == target:
                nonlocal answer
                answer += 1
            
        else:
            dfs(temp + numbers[index], index+1)
            dfs(temp - numbers[index], index+1)
    dfs(0, 0)
    return answer