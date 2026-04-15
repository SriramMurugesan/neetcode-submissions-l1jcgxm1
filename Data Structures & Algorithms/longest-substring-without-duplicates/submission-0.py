class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=0
        for i in range(len(s)):#3
            set1 = set()
            for j in range(i,len(s)):#2
                if s[j] in set1:#z
                    break
                set1.add(s[j])#{z,x,y}
            result=max(result,len(set1))#(3,3)
        return result