#U
    #input: [int] nums
    #output: int
    #constraints: no adjacent robberies, [1,100] houses, [0, 400] values
    #edge: 1 house
#P
    #dp[i] = max robbed at idx i
    #dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
    #dp is size nums+2 (first house robbed may not be 0)
    #dp[0], dp[1] = 0, 0
    #for i in range(2, len(nums)+2):
        #dp relation
    #return dp[-1]

def house_robber(nums: list[int]) -> int:
    dp = [0] * (len(nums)+2)
    dp[0], dp[1] = 0, 0
    for i in range(2, len(nums)+2):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])
    return dp[-1]

if __name__ == '__main__':
    print(house_robber([1,2,3,1]))
    print(house_robber([2,7,9,3,1]))
    print(house_robber([10]))
    
#O(N) time + O(N) mem