# ex2tron's blog:
# http://ex2tron.wang

import collections


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word_count = collections.Counter(word.strip("!?',;.")
                                         for word in paragraph.lower().split())
        result = ''
        for word in word_count:
            if (not result or word_count[word] > word_count[result]) and word not in banned:
                result = word
        return result
