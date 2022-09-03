class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) # 배열의 길이 
        temp = [i for i in range(n+1)]
        for i in nums:
            if i in temp:
                temp.remove(i)
        return temp[0]