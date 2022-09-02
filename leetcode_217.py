class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 딕셔너리 [key:value]
        check = {}
        for i in nums:
            if i in check.keys():
                check[i] += 1
            else:
                check[i] = 1
        
        # key 값이 2인것이 있으면 return true else false
        flag = False
        for i in check.values():
            if i >= 2:
                flag = True 
        return flag
            
        