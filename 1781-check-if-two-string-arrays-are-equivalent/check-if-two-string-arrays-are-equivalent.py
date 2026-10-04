class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        word = ''
        for i in range(len(word1)):
            word = word + str(word1[i])
            
        word2_str = ''
        for i in range(len(word2)):
            word2_str = word2_str + str(word2[i])
            
        return word == word2_str
