class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        
        for n in s:
            if n not in s_count:
                s_count[n] = 1
            else:
                s_count[n] += 1
        
        for m in t:
            if m not in t_count:
                t_count[m] = 1
            else:
                t_count[m] += 1
        
        return s_count == t_count
    #    s_set = Counter(s)
    #    t_set = Counter(t)
       
    #    return s_set==t_set
        