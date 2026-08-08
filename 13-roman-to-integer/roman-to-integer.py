class Solution:
    def romanToInt(self, n: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for i in range(len(n)):
            if i < len(n) - 1 and roman_map[n[i]] < roman_map[n[i + 1]]:
                total -= roman_map[n[i]]
            else:
                total += roman_map[n[i]]

        return total