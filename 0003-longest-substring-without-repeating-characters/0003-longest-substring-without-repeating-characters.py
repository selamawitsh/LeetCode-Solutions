class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_count = {}
        l = 0
        max_count = 0
        
        for i in range(len(s)):
            if s[i] in hash_count and hash_count[s[i]] >= l:
                l = hash_count[s[i]] + 1
            hash_count[s[i]] = i
            max_count = max(max_count, i - l + 1)
        
        return max_count
