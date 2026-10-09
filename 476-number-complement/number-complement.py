class Solution:
    def findComplement(self, num: int) -> str:
        binary = ""
        n = num
        
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2
            
        if not binary:
            binary = "0"
            
        l = list(binary)
        new1 = "0"
        new2 = "1"
        
        for i in range(len(l)):
            if l[i] == "0":
                l[i] = new2
            elif l[i] == "1":
                l[i] = new1
        num = int("".join(l),2)
        return num
