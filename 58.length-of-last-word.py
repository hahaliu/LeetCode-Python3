class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.rstrip().split(' ')
        return len(words[-1])


print(Solution().lengthOfLastWord("a "))
