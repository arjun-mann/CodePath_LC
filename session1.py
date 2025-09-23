#given:
    #write a function welcome
    #prints string "Welcome to The Hunded Acre Wood!"
    
from collections import deque


def welcome():
    print("Welcome to the Hundred Acre Wood!")
    
#problem 2:
#greeting()
#given: str name
    #prints string

def greeting(word: str):
    print("Welcome to The Hundred Acre Wood", word, "My name is Christopher Robin.")

#problem 3:
def print_catchphrase(word: str):
    fmap = {"Pooh" : "Oh brother!"}
    if word in fmap:
        print(fmap[word])
        
#problem 1:
#given: 
    #accepts list of items, and a target
    #return the first index of target in items and -1 if target is not in items


def linear_search(items, target):
    for i, val in enumerate(items):
        if val == target:
            return i
    return -1    

#problem 2:
#4 operations, 1 variable
#trouncy, poiuncy decrement value of tigger by 1

            
            
#session 2
#Tranpose Matrix
#Understand (IOCE)
    # swap rows and columns with a transpose
    # square matrix or non square matrix
    # I - [[int]] matrix
    # O - [[int]] 
    # C - NA
    # E - 
        #square matrix or non square matrix
        #[[]] empty
        #[[1]] 1 element
#P - plan
    #iterate row by row, and copy elements into a new matrix 
        #O(N*M) time + O(N*M) mem
#I - Implement (Key Idea, Steps)
    #iterate each row
        #iterate col until we reach the matching row index
            #i = 1, j = 0 <-> i = 0, j = 1
            #i = 2, j = 1 <-> i = 1, j = 2
    
    #n, m = len(matrix), len(matrix[0])
    #for i in range(n)
    
    #newmatrix = 
    #iterate each row
        #iterate each 
    
#problem 1:
# def transpose(matrix):
#     n, m = len(matrix), len(matrix[0 ])
#     newmatrix = [[0] * n for i in range(m)]
#     for i in range(n): #iterate rows
#         for j in range(m): #iterate cols
#             newmatrix[j][i] = matrix[i][j]
#     print(newmatrix)
            
#problem 2:
#U (IOCE)
    #input: [str] lst
    #output: [str]
    #constraint: no slicing (no reverse)
    #edge cases: empty, 1 element
#P
    #do 2 pointers, 1 from each edge, work inwards, doing swaps at 2 pointers
    #stop when they meet
#I (key idea, steps)
    #steps:
        #initialize left and right prs
        #while left < right
            #swap our left and right characters

def reverse_list(lst):
    left = 0
    right = len(lst)-1
    while(left < right):
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    print('1')
    return lst

#problem: 3
#remove duplicates:
#U
    #Input: [int] (sorted)
    #output: int (length) : [int] (duplicates removed)
    #constrint: inplace
    #edge case: empty, 1 el
#P
    #convert to set, return length
#I

#problem: 4
#Understand
    #Input: [int] nums
    #Output: 
       #moves all even integers to beginning of array, followed by odd integers
    #constriant: [int]
    #edge case:
#Plan
    #use deque, push even nums to start, odd nums to end
#Implent (Key Idea, steps)

def sort_by_parity(nums):
    d = deque()
    for n in nums:
        if n % 2 == 0:
            d.appendleft(n)
        else:
            d.append(n)
    return list(d)


def remove_dupes(items):
    ltos = set(items)
    return len(ltos)

#problem 5:
# U (IOCE)
    #input: [int] heights
        #heigts[i] = height of i
        #n vertical lines such that 2 endpts
            #ith line are (i, 0) and (i, heights[i])
        #find 2 lines, teogher with x, form container to store most honey
    #output: int
        #max amount of honey a containter can store
    #constraint: NA
    #edge case: empty, 1 element
# P
    #left 2 pointer 
# I

if __name__ == "__main__":
    # lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
    # print(reverse_list(lst))
    # print(1)
    
    # items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
    # print(remove_dupes(items))
    nums = [3, 1, 2, 4]
    print(sort_by_parity(nums))



    
    
    

    

    

    