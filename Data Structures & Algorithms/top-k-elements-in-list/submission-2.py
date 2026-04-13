class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = []

        for num in nums:
            if num not in mp:
                mp[num] = 1

            else:
                mp[num] += 1

        sorted_items = sorted(mp.items(),key = lambda x:(-x[1],-x[0]))

        for i in range(k):
            res.append(sorted_items[i][0])

        return res
        