class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 别人的代码
        temp = []
        dicts = {"{": "}", "(": ")", "[": "]"}
        for c in s:
            if c in dicts.keys():
                temp.append(c)
            elif len(temp) == 0 or dicts[temp.pop()] != c:
                return False
        return len(temp) == 0

        # if not s:
        #     return True
        # if len(s) % 2 != 0:
        #     return False
        # for i in range(len(s)):
        #     index = s[i+1:][::-1].find(dicts.get(s[i], "&"))
        #     if(index == -1 or (index - i) % 2 != 0):
        #         return False
        #     else:
        #         subs = s[i+1:index+1]
        #         return self.isValid(subs)


if __name__ == '__main__':
    print(str(Solution().isValid("(([]){})")).lower())
