class Solution:
    def trap(self, height: List[int]) -> int:
        length=len(height)
        area=0
        for i in range(length):#3
            left=height[i]#3
            right=height[i]#3
            for j in range(i):#
                left = max(left,height[j])#2
            for j in range(i+1,length):
                right = max(right,height[j])#(3)
            area += min(left,right)-height[i]
        return area
