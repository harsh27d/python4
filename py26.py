class Solution:
    def secondSmallest(self, nums):
        first = None
        second = None

        for num in nums:
            if first is None or num < first:
                second = first
                first = num
            elif num != first and (second is None or num < second):
                second = num

        return second


obj = Solution()
print(obj.secondSmallest([8, 3, 5, 1, 3, 7]))