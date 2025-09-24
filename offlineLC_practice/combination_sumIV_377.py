
def combinationSumIV(self, nums: List[int], target: int) -> int:
    #Understand
        #input: [int] nums, int target
            #given an array of distinct integers, and target int
            #return number of possible combinations that add up to target
            #test cases are generated so the answer can fit in 32-bits
        #output: int
        #constraints:1 <= num <= 200, 1 <= nums[i] <= 1000, 1 <= target <= 1000
        #edge: 1 el num
    #Plan
        #dp[i][j] = num of times we reach total j at idx i
        #dp[i][j] = tsum = total-nums[i]. dp[i][j] = dp[i-1][tsum]
        
        
        
    
        
    
    

if __name__ == "__main__":
    combinationSumIV