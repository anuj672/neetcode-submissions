class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if s and not t:
            return False

        if t and not s:
            return False

        if len(s)!=len(t):
            return False

        count_s = [0] * 26   
        for i in s:
            count_s[ord(i)-ord('a')]+=1

        count_t = [0] * 26   
        for i in t:
            count_t[ord(i)-ord('a')]+=1

        return count_s == count_t