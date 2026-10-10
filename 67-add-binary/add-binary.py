class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = list(a)
        j = list(b)
        suma = 0
        sumb = 0
        v = []
        for i in range(len(l)):
            suma+=int(l[len(l)-1-i])*(2**i)
        for k in range(len(j)):
             sumb+=int(j[len(j)-1-k])*(2**k)
        sumc = suma+sumb
        if sumc == 0:
            return "0"
        else:
            while sumc>0:
              v.append(str(sumc%2))
              sumc//=2
            v = v[::-1]
            return "".join(v)