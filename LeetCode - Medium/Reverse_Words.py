class Solution(object):
    def reverseWords(self, s):
        """
        Reverse words
        :type s: str
        :rtype: str
        """
        string = ""
        stack = []
        i = 0
        j = 0
        while (i < len(s)):
            if (s[i] == " "):
                if i > j:
                    stack.append(s[j:i])
                j = i + 1
            i += 1
        if (i > j):
            stack.append(s[j:i])
        while (len(stack) != 0):
            string += stack.pop() + " "
        return string.strip()
