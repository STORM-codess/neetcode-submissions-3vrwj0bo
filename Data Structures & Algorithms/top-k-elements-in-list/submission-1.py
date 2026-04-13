class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = 1

            else:
                mp[nums[i]]+=1

        for i in range(k):
            key = max(mp,key=mp.get)
            res.append(key)
            del mp[key]
        return res
        
        
                
        