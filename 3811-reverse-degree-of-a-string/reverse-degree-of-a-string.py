class Solution:
    def reverseDegree(self, s: str) -> int:
        
        reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
        ssum = 0
        pos = 1
        for letter in s:
            

            p_index = reversed_alphabet.index(letter)
            letter = p_index + 1
            product = letter * pos

            ssum = ssum + product
            

            pos +=1

        return ssum
