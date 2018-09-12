class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        x += moves.count('R') - moves.count('L')
        y += moves.count('U') - moves.count('D')
        return x == 0 and y == 0
