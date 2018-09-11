class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_array = str.split()
        if len(str_array) != len(pattern):
            return False
        dicts = {}
        for i in range(len(pattern)):
            if pattern[i] in dicts.keys():
                if dicts[pattern[i]] != str_array[i]:
                    return False
            elif str_array[i] in dicts.values():
                return False
            dicts[pattern[i]] = str_array[i]

        return True


print(Solution().wordPattern("abba", "dog cat cat dog"))
