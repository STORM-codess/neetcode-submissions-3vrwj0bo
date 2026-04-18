class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [0]*len(nums)
        contain_zero = False
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                contain_zero = True
                count +=1
                continue
            product*=nums[i]
        
        if count > 1:
            return res

        if count == len(nums):
            return res

        for i in range(len(nums)):
            if contain_zero == True:
                if nums[i] == 0:
                    res[i] = product

            else:
                res[i] = product//nums[i]

        return res



        