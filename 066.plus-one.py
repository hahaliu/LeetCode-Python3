# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if(digits[i] == 9):
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0
                break

        if carry == 1:
            digits = [1]+digits

        return digits


print(list(Solution().plusOne([1, 9, 9])))
