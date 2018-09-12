class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for i in range(left, right+1):
            if self.isSelfDividingNumber(i):
                ret.append(i)

        return ret

    def isSelfDividingNumber(self, n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in n_str:
            if n % int(i) != 0:
                return False
        return True


# 别人的代码：
# class Solution:
#     def selfDividingNumbers(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: List[int]
#         """
#         ret = []
#         for i in range(left, right+1):
#             if self.isSelfDividingNumber(i):
#                 ret.append(i)

#         return ret

#     def isSelfDividingNumber(self, n):
#         num = n
#         while num > 0:
#             if (num % 10) == 0 or (n % (num % 10)) != 0:
#                 return False
#             num //= 10
#         return True
