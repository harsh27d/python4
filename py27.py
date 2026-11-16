#Pgm to swap the first and last elements.
class Solution:
    def swapElements(self, nums):
        nums[0], nums[-1] = nums[-1], nums[0]
        return nums


obj = Solution()
print(obj.swapElements([10, 20, 30, 40]))