class Solution:
    def threeSum(self, nums):
        ans = set()
        n = len(nums)

        for i in range(n):

            seen = set()

            for j in range(i + 1, n):

                third = -(nums[i] + nums[j])

                if third in seen:

                    triplet = tuple(sorted([nums[i], nums[j], third]))

                    ans.add(triplet)

                seen.add(nums[j])

        return [list(t) for t in ans]