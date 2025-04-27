class Solution(object):
    def reverseVowels(self, s):
        """
        Reverse the position of vowels in a string
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        stack = []
        string = ""
        i = 0
        while(i < len(s)):
            if (s[i].lower() in vowels):
                stack.append(s[i])
            i += 1
        i = 0
        while(i < len(s)):
            if (s[i].lower() in vowels):
                string += stack.pop(-1)
            else:
                string += s[i]
            i += 1
        return string
