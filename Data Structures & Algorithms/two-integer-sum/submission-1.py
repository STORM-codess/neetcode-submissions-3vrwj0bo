class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        seen = {}
        for i in range(len(nums)):
            sec = target -  nums[i]
            if sec in seen:
                    res.append(seen[sec])
                    res.append(i)
                
                    return res
            
            else:
                seen[nums[i]] = i
            

        