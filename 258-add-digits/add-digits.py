class Solution:
    def addDigits(self, num: int) -> int:
        n = str(num)
        
        # Keep reducing as long as the string representation has more than 1 digit
        while len(n) > 1:
            l = []
            for i in n:
                l.append(i)
            
            total = 0
            for a in range(len(l)):
                total += int(l[a])
                
            n = str(total)  # Update n with the new sum to run again if needed
            
        return int(n)