#Move All Zeros to the End

class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        result = []

        for num in nums:
            if num != 0:
                result.append(num)

        while len(result) < len(nums):
            result.append(0)

        return result
