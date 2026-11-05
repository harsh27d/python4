class Solution:
    def moveZeroes(self, nums):
        result = []

        for num in nums:
            if num != 0:
                result.append(num)

        for num in nums:
            if num == 0:
                result.append(num)

        return result


obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))