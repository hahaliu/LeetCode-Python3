# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter_morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                        "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        ret_array = []
        for word in words:
            ret_array.append(
                "".join([letter_morse[ord(ch)-97] for ch in word]))

        return len(set(ret_array))
