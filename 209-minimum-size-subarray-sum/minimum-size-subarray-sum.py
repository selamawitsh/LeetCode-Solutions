class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum=0
        l=0
        min_window= float('inf')

        for r in range(len(nums)):
            current_sum+=nums[r]

            while current_sum>=target:
                min_window=min(min_window, r-l+1)
                current_sum-=nums[l]
                l+=1
        return min_window  if min_window != float('inf') else 0