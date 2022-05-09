class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i,num in enumerate(nums):
            if target-num in dict:
                sol = [dict[target-num], i]
                return sol
            
            dict[num] = i
                
            
