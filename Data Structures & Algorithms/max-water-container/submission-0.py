class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max=0
        while i<j:
            minH=min(heights[i],heights[j])
            curr=minH*(j-i)
            if max<curr:
                max=curr
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max