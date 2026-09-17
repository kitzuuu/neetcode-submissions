class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        charArray = [0]*26
        for letter in s:
            charArray[ord(letter)-97]+=1
        for letter in t:
            charArray[ord(letter)-97]-=1  
        for i in charArray:
            if i != 0:
                return False
        return True