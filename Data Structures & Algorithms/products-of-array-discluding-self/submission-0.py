class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] *  n #[0,0,0,0]   [1,2,4,6]

        for i in range(n): #0
            x = 1
            for j in range(n): #3
                if i == j:
                    continue
                x = x*nums[j] #48
            result[i] = x
        return result


        