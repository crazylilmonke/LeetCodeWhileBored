class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        l = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                l.append(i)
                if i != 1 and i * i != num:
                    l.append(num // i)

        return sum(l) == num