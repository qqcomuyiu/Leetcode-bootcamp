class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        out=float("-inf")
        while left<right:
            out=max(out,(right-left)*min(height[right],height[left]))
            if height[left]<height[right]:
                left+=1  
            else:
                 right-=1
        return out
        