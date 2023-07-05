class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        answer = ""
        i = 0
        while i < min(len(word1), len(word2)):
            answer = answer + word1[i] + word2[i]
            i += 1
        if len(word1) < len(word2):
            answer = answer + word2[i:]
        else:
            answer = answer + word1[i:]
        return answer
