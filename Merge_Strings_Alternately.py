class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        Merge 2 string by adding letters in Alternating order
        :type word1: str
        :type word2: str
        :rtype: str
        """
        string = ""
        index = 0
        while(index < len(word1) and index < len(word2)):
            string += word1[index]
            string += word2[index]
            index += 1
        string += word1[index:len(word1)]
        string += word2[index:len(word2)]
        return string
