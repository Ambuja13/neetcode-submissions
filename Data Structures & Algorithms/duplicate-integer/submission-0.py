class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_set = set(nums)
        if len(nums) > len(distinct_set):
            return True
        else:
            return False
