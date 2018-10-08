# ex2tron's blog:
# http://ex2tron.wang


# 我的写法：太复杂
# class Solution:
#     def findAndReplacePattern(self, words, pattern):
#         """
#         :type words: List[str]
#         :type pattern: str
#         :rtype: List[str]
#         """
#         ret = []
#         match = True
#         for word in words:
#             if len(word) == len(pattern):
#                 dicts = {pattern[0]: word[0]}
#                 for i in range(1, len(word)):
#                     if pattern[i] in dicts.keys():
#                         match = dicts[pattern[i]] == word[i]
#                     else:
#                         if word[i] in dicts.values():
#                             match = False
#                             break
#                         else:
#                             dicts[pattern[i]] = word[i]

#                 if match:
#                     ret.append(word)

#         return ret

# 别人的代码：
# 用到setdefault，filter


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            lookup = {}
            for x, y in zip(pattern, word):
                if lookup.setdefault(x, y) != y:
                    return False
            return len(set(lookup.values())) == len(lookup.values())

        return list(filter(match, words))


# print(Solution().findAndReplacePattern(
#     ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
print(Solution().findAndReplacePattern(
    ["fcvxuskhcl"], "rdzkpkbmda"))
