#U
    #input: [int] nums
        #each house has a certain amount of money stashed
        #all houses at this place are arranged in a circle
    #output:
    #constraint: no adjacent houses + (first AND last house)
        #[1, 100] houses, [0, 1000] values
    #edge: 1 house
#P:
    #dp[i] = max robbed at idx i
    #dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        #2 pass: [0, len-1) + [1, len)
        
    #create dp of size n+2 (fill with 0)
    #for i in range(2, len(n)+1) STOP BEFORE LAST
        #dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
    #last = dp[-1]
    
    #create dp of size n+2 (fill with 0)
    #for i in range(3, len(n)+2) SKIP FIRST
        #dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
    #reutrn max(last, dp[-1])

def house_robberII(nums: list[int]) -> int:
    dp = [0] * (len(nums)+2)
    for i in range(2, len(nums)+1):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
    last = dp[-2]
    print(dp)
    dp = [0] * (len(nums)+2)
    for i in range(3, len(nums)+2):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
    print(dp)
    return max(last, dp[-1])

if __name__ == '__main__':
    print(house_robberII([2,3,2]))
    print(house_robberII([1,2,3,1]))
    
