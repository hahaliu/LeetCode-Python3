# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dicts = {}
        for i in range(len(s)):
            if s[i] not in dicts.keys():
                if t[i] in dicts.values():
                    return False
                dicts[s[i]] = t[i]
            else:
                if dicts[s[i]] != t[i]:
                    return False

        return True
