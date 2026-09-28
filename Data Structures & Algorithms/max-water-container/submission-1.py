class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxx=0
        while i<j:
            maxx=max(maxx,min(heights[i],heights[j])*(j-i))
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxx