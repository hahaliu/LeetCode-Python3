import math


# 别人的方式：
# 厄拉多塞筛法
# （1）先把1删除（现今数学界1既不是质数也不是合数）
# （2）读取队列中当前最小的数2，然后把2的倍数删去
# （3）读取队列中当前最小的数3，然后把3的倍数删去
# （4）读取队列中当前最小的数5，然后把5的倍数删去
# （5）读取队列中当前最小的数7，然后把7的倍数删去
# （6）如上所述直到需求的范围内所有的数均删除或读取

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        prime = [1]*n
        prime[0] = prime[1] = 0
        for i in range(2, int(n**0.5)+1):
            if prime[i] == 1:
                prime[i*i:n:i] = [0]*len(prime[i*i:n:i])
        return sum(prime)


# 传统方法：会超时


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n):
            prime = True
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                count += 1

        return count


print(Solution().countPrimes(10))
