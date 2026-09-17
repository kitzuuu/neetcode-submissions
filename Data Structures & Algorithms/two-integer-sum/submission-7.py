class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        arr=[0,0]
        while True:
            need = target - nums[i]
            if need in nums:
                j=len(nums)-1
                while need != nums[j]:
                    j-=1
                arr=[i,j]
                if i != j : 
                    break
            i+=1
        return arr