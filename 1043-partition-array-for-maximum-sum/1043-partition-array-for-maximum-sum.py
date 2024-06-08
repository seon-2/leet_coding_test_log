class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        
        for i in range(n):
            current_max = 0
            # 고려할 부분 배열의 최대 길이는 k
            for j in range(1, k + 1):
                if i - j + 1 >= 0:
                    current_max = max(current_max, arr[i - j + 1])
                    if i - j >= 0:
                        dp[i] = max(dp[i], dp[i - j] + current_max * j)
                    else:
                        dp[i] = max(dp[i], current_max * j)
        
        return dp[-1]
