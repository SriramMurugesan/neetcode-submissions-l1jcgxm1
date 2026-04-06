class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D={}
        for i,num in enumerate(nums):
          complement=target-num
          if complement in D:
            return [D[complement],i]
          D[num]=i
        return []
