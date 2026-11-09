class Solution:
    def firstUniqChar(self, s):
        for ch in s:
            if s.count(ch) == 1:
                return ch

        return -1


obj = Solution()
print(obj.firstUniqChar("leetcode"))
print(obj.firstUniqChar("aabb"))