class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        sum = 0
        for i in range(len(num)):
            sum += num[i] * (10 ** (len(num) - i - 1))
            
        sum += k
        j = []
        while sum > 0:
            rem = sum % 10
            sum = sum // 10
            j.append(rem)
            
        return j[::-1]
