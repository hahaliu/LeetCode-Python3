# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = value = 0
        for i in range(max(len(a), len(b))):
            value = carry
            if (i < len(a)):
                value += int(a[-(i+1)])
            if(i < len(b)):
                value += int(b[-(i+1)])
            carry, value = value//2, value % 2
            result += str(value)

        if carry:
            result += str(carry)
        return result[::-1]


print(Solution().addBinary("1010", "1011"))
