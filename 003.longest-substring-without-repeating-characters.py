class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_lst = []

        result = 0
        for ch in s:
            max_lst.append(ch)
            if len(set(max_lst)) < len(max_lst):
                max_lst = max_lst[max_lst.index(ch)+1:]
            result = max(result, len(max_lst))

        return result


print(Solution().lengthOfLongestSubstring("dvdf"))
