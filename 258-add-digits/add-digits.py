class Solution:
    def addDigits(self, num: int) -> int:
        n = str(num)
        
       
        while len(n) > 1:
            l = []
            for i in n:
                l.append(i)
            
            total = 0
            for a in range(len(l)):
                total += int(l[a])
                
            n = str(total)  
            
        return int(n)