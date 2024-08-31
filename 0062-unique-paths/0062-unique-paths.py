class Solution:
    import math
    
    def uniquePaths(self, m: int, n: int) -> int:
        
#         grid = []
        
#         for i in range(m):
#             temp = []
#             for j in range(n):
#                 if i == 0 or j == 0:
#                     path_number = 1
#                 else:
#                     path_number = 0
#                 temp.append(path_number)
#             grid.append(temp)
        
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

#         return grid[m-1][n-1]
        
        return math.factorial(m+n-2) // (math.factorial(m-1) * math.factorial(n-1))