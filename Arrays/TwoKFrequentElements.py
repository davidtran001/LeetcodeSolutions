class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            count[num] = 1 + count.get(num,0)
         
        bucket = [[] for i in range(len(nums)+1)]
        
        for key, v in count.items():
            bucket[v].append(key)
        
        solu = []
        
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                solu.append(num)
                if len(solu) == k:
                    return solu
                