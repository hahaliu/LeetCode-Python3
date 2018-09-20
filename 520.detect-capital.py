class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word==word.upper() or word==word.title() or word==word.lower()
        # 其他写法：
        # return  word.isupper() or word.islower() or word.isupper()56.5%