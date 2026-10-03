class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = num
        count = 0
        while n > 0:
            if n % 2 == 0:
                n = n // 2  # Used integer division to keep it as an int type
            else:
                n = n - 1
            count += 1
        return count
