class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        
        for c in s:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
                
        for c in t:
            if c not in dict: return False
            
            elif c in dict:
                dict[c] -= 1
                if dict[c] == 0:
                    dict.pop(c)
                    
        if dict: return False
        return True

# hashmap tracks count of each char in s, if t has the exact same count then True 