class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = {}
        def count(n, last_char):
            if n == 0:
                return 1
            if (n, last_char) in dp:
                return dp[(n, last_char)]
            
            total = 0
            for c in ['a', 'e', 'i', 'o', 'u']:
                if c >= last_char:
                    total += count(n-1, c)
            
            dp[(n, last_char)] = total
            return total
    
        return count(n, 'a')