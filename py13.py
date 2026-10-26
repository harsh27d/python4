#Find the Second Largest Distinct Number

class Solution:
    def secondLargest(self, nums: list[int]) -> int:
        unique = list(set(nums))
        unique.sort()

        if len(unique) < 2:
            return -1

        return unique[-2]
