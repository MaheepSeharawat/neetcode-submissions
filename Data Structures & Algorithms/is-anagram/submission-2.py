class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        has1=Counter(s)
        has2=Counter(t)
        return has1==has2