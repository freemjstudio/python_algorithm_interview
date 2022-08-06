def solution(nums):
    answer = 0
    temp_dict = {}
    for i in nums:
        if i in temp_dict.keys():
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1
    n = len(nums)
    if len(temp_dict) >= n//2:
        answer = n//2
    else:
        answer = len(temp_dict)
    return answer