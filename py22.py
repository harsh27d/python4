class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)


obj = Solution()
print(obj.missingNumber([0, 1, 3, 4, 5]))