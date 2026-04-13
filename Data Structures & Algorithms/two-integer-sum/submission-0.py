class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        seen = {}
        for i in range(len(nums)):
            sec = target -  nums[i]
            if sec in seen:
                if seen[sec]<i:
                    res.append(seen[sec])
                    res.append(i)
                else:
                    res.append(i)
                    res.append(seen[sec])

                return res
            
            else:
                seen[nums[i]] = i
            

        