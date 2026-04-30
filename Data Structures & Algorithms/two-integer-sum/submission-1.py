class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            sol=target-nums[i]
            if sol in d.keys() and i!=d[sol]:
                return [i,d[sol]]
        return [-1,-1]