class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        ogset = set()  

        
        while num != "1" and num not in ogset:
            ogset.add(num)
            res = 0
            
           
            for i in num:
                res = res + (int(i) ** 2)
                
            num = str(res)

        return num == "1"
