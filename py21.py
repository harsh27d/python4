class Solution:
    def secondLargest(self, arr):
        first = second = -1

        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num

        return second


obj = Solution()
print(obj.secondLargest([10, 20, 5, 30, 15]))