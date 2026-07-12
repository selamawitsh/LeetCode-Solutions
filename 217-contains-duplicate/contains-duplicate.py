class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(set(nums))!=len(nums):
        #     return True
        # else:
        #     return False

        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True
        return False
        

