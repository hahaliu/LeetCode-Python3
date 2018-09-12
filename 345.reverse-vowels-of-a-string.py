class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
        s_vowels = [ch for ch in s if ch in vowels][::-1]
        s_array, index = list(s), 0
        for i in range(len(s_array)):
            if s_array[i] in vowels:
                s_array[i] = s_vowels[index]
                index += 1

        return ''.join(s_array)


print(Solution().reverseVowels("aA"))
