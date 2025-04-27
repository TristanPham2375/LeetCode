class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        Finds the Greatest Common Divisor of two strings
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        while str2:
            if str1.startswith(str2):
                str1 = str1[len(str2):]
            else:
                str1, str2 = str2, str1

        return str1
