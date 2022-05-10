class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solu = []

        # compute prefixes
        prefix = 1
        for num in nums:
            solu.append(prefix)
            prefix *= num

        # compute postfixes
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            solu[i] *= postfix
            postfix *= nums[i]

        return solu

# for each num calculate prefix and postfix -> prefix * postfix = product except num