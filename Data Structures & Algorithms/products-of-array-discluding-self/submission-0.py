class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        i=0
        prefix = [0]*length
        suffix = [0]*length
        temp=1
        while i < length:
            temp*=nums[i]
            prefix[i]=temp
            i+=1
        temp=1
        i-=1
        while i >= 0:
            temp*=nums[i]
            suffix[i]=temp
            i-=1
        nums[0]=suffix[1]
        nums[length-1]=prefix[length-2]
        for i in range(1, length-1):
            nums[i]=prefix[i-1]*suffix[i+1]
        return(nums)
        