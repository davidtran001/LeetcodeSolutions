class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs) -> str:
        # O(n)
        return ''.join(
            f'{len(string)}#{string}'
            for string in strs
        )

# encode s.t the encoding can gives info about len of each string 

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

# since encode tells us length of each string prior, decode using this info