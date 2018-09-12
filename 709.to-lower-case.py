class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # 使用内建函数：
        # return str.lower()
        # 不适用内建函数：
        return "".join([chr(ord(ch)+32) if 'A' <= ch <= 'Z' else ch for ch in str])
