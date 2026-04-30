class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        s=Counter(nums)
        for i in s.keys():
            if (s[i]>=2):
                return True
        return False