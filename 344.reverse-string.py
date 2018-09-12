class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 使用内建函数
        # return s[::-1]
        # 不使用内建函数
        s_array = list(s)
        for i in range((len(s_array)+1)//2):
            s_array[i], s_array[~i] = s_array[~i], s_array[i]

        return ''.join(s_array)
