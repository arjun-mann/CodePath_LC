#U
    #input: str s
        #message encoded as nums
        #message decoded w/ mapping
        #multiple possible decodings
    #output: int
        #num of ways to decode it
        #if not decodable, return 0
    #constraint: slen [1, 100]
    #edge: 1 element, can't decode
#P
    #dp[i] = total encodings at idx i
    #dp[i] = dp[i-1] + 2,1,or 0 depending on s[i] and s[i-1]

    #dp of size s+1 (s[0] can be > 0)
    #for i in range(1, len(s)+1)
        #recurrence relation
        
        #i-1 >= 0 and nums[i-1] is [1,2]:
        
        #plus = 0
        #if nums[i-1] == 1
            #plus += 1
        #if nums[i-1] == 2 and nums[i] is [0,6]
            #plus += 1
        #if (i == 0 or (nums[i-1] != 1 and nums[i-1] != 2) and nums[i] == 0
            #return 0
        #if nums[i] != 0:
            #plus += 1
        #dp[i] = dp[i-1] + nums
        
        
        
    #return dp[-1]
    
def decode_ways(s: str) -> int:
    dp = [0] * (len(s)+1)
    dp[0] = 1
    for i in range(1, len(s)+1):
        plus = 0
        if i > 1 and s[i-2] == '1':
            plus += 1
        if i > 1 and s[i-2] == '2' and s[i-1] in ('0', '1', '2', '3', '4', '5', '6'):
            plus += 1
        if s[i-1] == '0' and (i == 1 or (s[i-2] != '1' and s[i-2] != '2')):
            return 0
        dp[i] = dp[i-1] + plus
    print(dp)
    return dp[-1]
    
if __name__ == '__main__':
    print(decode_ways('12'))
    print(decode_ways('226'))
    print(decode_ways('06'))
    
    