class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        basic = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

        basic_sort, ret = sorted(basic.keys(), reverse=True), []

        while num > 0:
            for v in basic_sort:
                if num//v > 0:
                    num -= v
                    ret.append(basic[v])
                    break
        return ''.join(ret)


print(Solution().intToRoman(60))
