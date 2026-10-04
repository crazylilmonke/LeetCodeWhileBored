class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        n = len(arr)
        counts = [arr.count(x) for x in arr]

        no = None
        for i in range(n):
            for j in range(n):
                if counts[i] == counts[j] and arr[i] != arr[j]:
                    no = True
                    
        if no == True:
            return False
        else:
            return True
