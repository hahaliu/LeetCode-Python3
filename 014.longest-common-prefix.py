class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        i = 0
        for i in range(len(strs[0])):
            c = strs[0][i]
            lst = [True if i <= len(item)-1 and item[i]
                   == c else False for item in strs[1:]]
            if False in lst:
                break
            i += 1
        return strs[0][:i]


if __name__ == '__main__':
    print(Solution().longestCommonPrefix([""]))
