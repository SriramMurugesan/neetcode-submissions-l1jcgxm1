class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x=set()
        nums.sort()#[-4,-1,-1,0,1,2]
        for i in range(len(nums)):#2
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1# two pointer approach
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    x.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return [list(i) for i in x]
