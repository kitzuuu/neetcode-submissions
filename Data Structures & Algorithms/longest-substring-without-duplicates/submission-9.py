class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=[]
        maxLength=0
        i=0
        while i < len(s):
            c=s[i]
            sub.append(c)
            if  sub.index(c)!=len(sub)-1:
                sub=sub[sub.index(c)+1:]
            maxLength=max(maxLength,len(sub))
            i+=1
        return maxLength