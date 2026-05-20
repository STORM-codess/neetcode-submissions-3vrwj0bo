class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        res = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                res.append(left+1)
                res.append(right+1)
                return res

            elif numbers[left] + numbers[right] < target:
                left += 1

            else:
                right -= 1

            