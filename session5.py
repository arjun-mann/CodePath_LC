

#IIIDIDDD
#I
#smallest used: _
#out: 1

#II
#smallest used: 1
#out: 12

#III
#smallest used: 2
#out: 123 (smallest used + 1)

#IIID
#smallest used: 3
#stack: D
#out: 123

#IIIDI
#smallest used: 3
#stack: D
#out: 123 (while stack is not empty, append len(stack) + smallest used + 1)
#out: 1235 (len stack was 1, now its empty)
#out: 12354 (smallest used + 1)

#IIIDIDDD
#smallest used: 3
#stack: D
#out: 123 (while stack is not empty, append len(stack) + smallest used + 1)
#out: 1235 (len stack was 1, now its empty)
#out: 12354 (smallest used + 1)

#start with empty stack
#I 
#append char
#start with empty stack
#if first char is I, append 1 to our stack
#if first char is D, append len(str)+1 to our stack

#first char is I
    #[1]
#next char is I
    #[1, 2]
#3rd char is D
    #[1, 2, ]
#append the len of substring 

#Understand
    #input: [str] arrival_pattern
        #organizing a prestigious event
        #organize order guests arrive based on instructions
        #0-indexed string arrival_pattern of length n
        #'I' - next guest should have a higher num than previous guest
        #'D' - next guest should have a lower num than previous guest
        #create str guest_order of len n+1 satisfying:
            #contains each num from 1 to str(n+1)
            #these numbers represent the guests' assigned numbers
            #for idx i from [0, n-1]
                #arrival_pattern[i] == 'I': guest_order[i] < guest_order[i+1]
                #arrival_pattern[i] == 'D': guest_order[i] > guest_order[i+1]
    #output: str
    #constraint: 
    #edge: len 0
#Plan
    #result = []
    #d_stack = []
    #smallest_used = 0
    #for ch in arrival_pattern
        #if ch == "I":
            #while (!d_stack.empty()):
                #result.append(len(stack) + smallest_used + 1)
                #d_stack.pop()
            #result.append(smallest_used + 1)
        #if ch == "D":
            #d_stack.append('D')
    #while !d_stack.empty():
        #result.append(len(stack) + smallest_used)
    #return ''.join(result)

def arrange_guest_arrival_order(arrival_pattern):
    result = []
    d_stack = []
    largest_used = 0
    for ch in arrival_pattern: #IIIDI
        if ch == 'I':
            # temp = 0
            temp = max(largest_used, len(d_stack) + largest_used + 1)
            while (d_stack): #stack: D
                result.append(str(len(d_stack) + largest_used + 1))
                # temp = max(largest_used, len(d_stack) + largest_used + 1)
                d_stack.pop()
            result.append(str(largest_used + 1)) #res: 1,2,3,5
            largest_used = temp #lu: 3
        if ch == "D":
            d_stack.append('D') #stack
    temp = max(largest_used, len(d_stack) + largest_used)
    while d_stack:
        result.append(str(len(d_stack) + largest_used))
        d_stack.pop()
    largest_used = max(temp, largest_used) #lu: 3
    return ''.join(result)

# if __name__ == '__main__':
print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))

# iterate through all chars in str
# if i -> append to answer
# if d -> append to stack
# if hit an i --> pop off all elements stack, add them to answer, then add elem[i] to ans

"""
def arrange_guest_arrival_order(arrival_pattern):
    stack = []
    answer = []  
    nums = list(range(1, len(arrival_pattern) + 1))
    #print(nums)
    for idx, char in enumerate(arrival_pattern):
        print(idx, char)
        if char == "I":
            while stack:
                answer.append(stack.pop())
            answer.append(str(nums[idx]))

        elif char == "D":
            stack.append(str(nums[idx]))

    while stack:
        answer.append(stack.pop())

    return ''.join(answer)

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))

"""

#Yay it works! :)

# omg yay good job
# i coudlnt fix mine lol its likeoff by 1 D: