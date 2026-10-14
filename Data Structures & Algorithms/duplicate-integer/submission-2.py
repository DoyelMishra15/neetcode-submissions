class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans=set()
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.add(nums[i])
            else:
                return True
        else:
            return False