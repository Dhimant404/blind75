# Un-optimised code
class Solution(object):
    def gcdOfStrings(self, strFirst, strSecond):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if strFirst > strSecond:
            str1 = strFirst
            str2 = strSecond
        else:
            str2 = strFirst
            str1 = strSecond

        biggi = ""
        for i in range(len(str2)):
            for j in range(0, len(str2) - i):
                if (len(str1) // (i + 1)) * str2[j : j + i + 1] == str1 and (
                    len(str2) // (i + 1)
                ) * str2[j : j + i + 1] == str2:
                    biggi = str2[j : j + i + 1]
        return biggi


# Optimesed solution
class Solution2(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        answer = ""
        len1, len2 = len(str1), len(str2)
        for i in range(1, min(len1, len2) + 1):
            if len1 % i == 0 and len2 % i == 0:
                if (
                    str1[:i] * (len(str1) / i) == str1
                    and str1[:i] * (len(str2) / i) == str2
                ):
                    answer = str1[:i]

        return answer
