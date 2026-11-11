class Solution:
    def longestWord(self, s):
        words = s.split()
        longest = ""

        for word in words:
            if len(word) > len(longest):
                longest = word

        return longest


obj = Solution()
print(obj.longestWord("Python makes coding interesting"))