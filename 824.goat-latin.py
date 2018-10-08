# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = "aoieu"
        S_array = S.split()
        return " ".join([S_array[i]+"ma"+"a"*(i+1) if S_array[i][0].lower() in vowel else S_array[i][1:]+S_array[i][0]+"ma"+"a"*(i+1) for i in range(len(S_array)) ])    