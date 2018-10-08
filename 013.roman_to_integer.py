# ex2tron's blog:
# http://ex2tron.wang

class Solution(object):

    # 别人的代码：
    # def romanToInt(self, s):
    #     numeral_map = {"I": 1, "V": 5, "X": 10,
    #                    "L": 50, "C": 100, "D": 500, "M": 1000}
    #     decimal = 0
    #     for i in range(len(s)):
    #         if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
    #             decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
    #         else:
    #             decimal += numeral_map[s[i]]
    #     return decimal

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        sc = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        result = 0
        i = 0
        while True:
            if(i > len(s)-1):
                break
            if(i != len(s)-1 and s[i]+s[i+1] in sc.keys()):
                result += sc[s[i]+s[i+1]]
                i += 2
            else:
                result += dicts[s[i]]
                i += 1
        return result


if __name__ == '__main__':
    print(Solution().romanToInt('LVIII'))
