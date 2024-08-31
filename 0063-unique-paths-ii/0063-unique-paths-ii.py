class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # 시작점에 장애물이 있는 경우
        if obstacleGrid[0][0] == 1:
            return 0
        
        # DP 배열 초기화
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        
        # 첫 번째 행 초기화
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # 첫 번째 열 초기화
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # 나머지 그리드 채우기
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]