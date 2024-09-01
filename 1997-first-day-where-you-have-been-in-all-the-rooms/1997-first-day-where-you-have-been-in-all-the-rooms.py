class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        MOD = 10**9 + 7
        
        # dp[i]: i번 방에 처음 도착하는 날짜
        dp = [0] * n
        
        for i in range(1, n):
            dp[i] = (2 * dp[i-1] - dp[nextVisit[i-1]] + 2) % MOD
            
            # i번 방에 처음 도착하는 날짜 계산
            # 1. i-1번 방에 처음 도착한 날짜
            # 2. i-1번 방에서 nextVisit[i-1]로 가는데 걸리는 시간 (홀수 번째 방문)
            # 3. nextVisit[i-1]에서 다시 i-1번 방으로 돌아오는데 걸리는 시간 (짝수 번째 방문)
            # 4. i-1번 방에서 i번 방으로 가는데 1일
        
        return dp[n-1]