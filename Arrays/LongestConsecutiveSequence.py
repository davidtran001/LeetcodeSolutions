class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
            
        mx = 0
        for num in nums:
            if num-1 not in unique:
                count = 0
                while num+count in unique:
                    count += 1
                mx = max(mx, count)
        return mx