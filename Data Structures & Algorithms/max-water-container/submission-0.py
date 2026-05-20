class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        max_water = 0
        curr_len = n-1

        while left < right:
            min_container = min(height[left],height[right])
            max_water = max(max_water,(min_container * curr_len))

            if height[left] < height[right]:
                left += 1

            else:
                right-=1

            curr_len -=1

        return max_water
        