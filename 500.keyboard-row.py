# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret = []

        all_chs = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for word in words:
            for chs in all_chs:
                if all([letter in chs for letter in word.lower()]):
                    ret.append(word)
                    continue
        return ret
