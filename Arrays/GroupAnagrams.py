class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            dict[tuple(count)].append(s)
            
        return dict.values()

# hashset hashed with tuples that take the count of each character in each string and group matching ones together