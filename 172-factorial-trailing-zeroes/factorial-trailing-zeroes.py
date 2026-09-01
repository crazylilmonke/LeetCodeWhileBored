import sys
sys.set_int_max_str_digits(100000)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
        
        z = fact(n)
        l = []
        for i in str(z):
            l.append(i)
        
        count = 0
        for i in reversed(l):
            if i == '0':
                count += 1
            else:
                break
        
        return count