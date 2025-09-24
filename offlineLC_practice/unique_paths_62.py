#U
    #input: int m, int n
        #m x n grid, start at top left
        #goal is to reach bottom right
    #output: int
        #num of possible unique paths
    #constraint: m and n [1, 100]
    #edge: 1 cell -> 1
#P
    #dp[i] = total paths to index i
    #dp[i] = dp[i][j-1] + dp[i-1][j]
    
    #create dp of size m+1 * n+1
    #initialize dp[0,1] and dp[1,0] to 1, and rest to 0
    #for i in range(1, m+1)
        #for j in range(1, n+1)
            #recursive relation
    #return dp[m][n]
    
def unique_paths(m: int, n: int):
    dp = [[0] * (n+1) for i in range(m+1)]
    dp[0][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m][n]
    
if __name__ == '__main__':
    print(unique_paths(3, 7))
    print(unique_paths(1, 1))
    print(unique_paths(3, 2))
    
    
