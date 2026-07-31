class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3,4,5,6 = 7
        for i in range(len(nums)):#i=2 
            for j in range(i+1,len(nums)):#3
                if target==nums[i]+nums[j]:
                    return [i,j]
        return []