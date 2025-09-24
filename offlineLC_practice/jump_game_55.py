#U
    #input: [int] nums
        #given int array nums, start at idx 0
        #each element is max jump len at that position
    #output: T/F
        #true if you can reach the last index, false otherwise
    #constraint:
    #given:
#P
    #dp[i] = you can reach idx i 
    #dp[i] = T if for j in range(0, i) if dp[j] == T and j+nums[j] == i
    
    #dp of size nums (el i always reachable)
    #for i in range(1, i)
        #for j in range(1, i):
            #recurrence relation
    #return dp[-1]
    
def jump_game(nums: list[int]) -> int:
    dp = [False] * len(nums)
    dp[0] = True
    for i in range(1, len(nums)):
        for j in range(1, i):
            if j+nums[j] == i and dp[j]:
                dp[i] = True
    print(dp)
    return dp[-1]

    
if __name__ == '__main__':
    print(jump_game([2,3,1,1,4]))
        