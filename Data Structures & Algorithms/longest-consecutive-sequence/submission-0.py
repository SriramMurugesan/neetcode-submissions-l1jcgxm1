class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x=0
        a=set(nums)#2,20,4,10,3,5
        for num in nums:#5
            b=num#5
            s=0
            while b in a:#3
                s+=1#1
                b+=1#6
            x = max(x,s)#(4,1),#4
        return x
            
            
