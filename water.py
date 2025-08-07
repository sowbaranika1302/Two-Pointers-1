# Container with Most Water
# Using the Two Pointers Technique
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,h = 0,len(height)-1
        while l<h:
            res = max(res,min(height[l],height[h])*(h-l))
            if height[l]<height[h]:
                l+=1
            else:
                h-=1
        return res


        