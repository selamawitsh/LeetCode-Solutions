class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen_index={}
        for i in range(len(nums)):
            if nums[i] in last_seen_index:
                if abs(last_seen_index[nums[i]]-i) <=k:
                    return True
            last_seen_index[nums[i]]=i
        return False
