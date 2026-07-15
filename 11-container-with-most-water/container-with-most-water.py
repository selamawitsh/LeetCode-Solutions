class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        max_area=0

        while l<r:
            min_height=min(height[l], height[r])
            area=min_height * abs(r-l)
            max_area=max(max_area, area)

            if l<r and height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return max_area

        