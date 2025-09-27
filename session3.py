
from collections import defaultdict

#Understand
    #input: string : int treasure_map
        #several clues point to locations
        #clue associated with:
            #location
            #num of treasures bured there
        #given dic treasure_map
            #key: locaion names
            #val: int represent num of treasures buried
        #return total num treasures buried
    #output: int
    #constraint:
    #edge:
#Plan

#problem 1
def total_treasure(treasure_map):
    sum = 0
    for val in treasure_map.values():
        sum += val
    return sum
    
#problem 2:
#U
    #input: str message
        #smuggle message
        #trust message if it contains letters in the alphabet
        #str message: containing only lowercase english letters and whitespace
        #return T/F if message contains every letter once, F otherwise
    #output: T/F
    #constraint: only lowercase letters + spaces
    #edge
#P

def can_trust_message(message):
    chars = set(message)
    if ' ' in chars:
        return len(chars) == 27
    return len(chars) == 26
        

#problem 3:
#U
    #input: [int]
        #[int] chests of len n
        #all int in chests are range [1, n]
            #each int appears once or twice.
        #Return an array of all integers that appear twice
    #output: [int]
    #constraint:
    #edge: empty
#P
#create our freqmap
#for val in chests
    #do += 1 to freqmap[val]
    #result = []
    #if freqmap[val] == 2:
        #append it to our result
    #return result

def find_duplicate_chests(chests):
    freqmap = defaultdict(int)
    result = []
    for val in chests:
        freqmap[val] += 1
        if freqmap[val] == 2:
            result.append(val)
    return result

#problem 4:
#U
    #input: str
        #secret code written in pirate language
        #trap disarmed if code balanced
            #balanced code: freq of every letter present is equal
            #to disable, remove exactly 1 letter from the message
        #determine if its possible to remove 1 letter to balance the pirate code
        #given 0-index str code, consisting of lowercase english
        #return T if 1 letter can be removed to validate, else False
    #output: T/F
    #constraint:
    #edge case: empty
#P
    #create our freqmap 
    #lowest count (uniform if valid)
    
    #2nd pass
    #iterate our freqmap
        #make sure 1 val has frequency low+1 (return False if dif val)
        #anything key val pair where val is any other val than low, return Flase
    #return True
    

        
    #sum all freqmap.vals
    #subtract by low*len
    
    #10 - 9 = 1 (== 1 return True)
    #a: 3
    #b: 3
    #c: 4
    
    #10 - 8 = 2 (!= 1 return False)
    #a: 3
    #b: 3
    #c: 2
    #d: 2
    
    #7 - 6 = 1  (1 return True)
    #b: 3
    #c: 2
    #d: 2
    
def can_make_balanced(code):
    freqmap = defaultdict(int)
    low = float('inf')
    if not code:
        return False
    for ch in code:
        freqmap[ch] += 1
        low = min(low, freqmap[ch])
    
    sumvals = 0
    for val in freqmap.values():
        sumvals += val
        sumvals -= low
    return sumvals == 1

#problem 5
#total = sum(v for v in my_dict.values() if v > 15)

# from collections import Counter
# freq = Counter(my_str)

#U
    #input:
        #num on map corresponds to amount of gold at location
            #list of gold amounts at various hidden locations
        #each num on the map corresponds to amount of gold at a specific location
        #want to find 2 distinct locations where sum at 2 locations == amount of space on ship
        #given [int] gold_amounts, target
            #amt of gold at each location
        #return idnices of 2 locations whose gold amount of gold adds up target
    #output:
    #constraint:
    #edge
#P
    #create our map (values to indices)
    #iterate gold)amounts
        #if target - gold_amounts[i] in map
            #return (i, map[target-gold_amounts[i]])
        #map[val] == idx

def find_treasure_indices(gold_amounts, target):
    vtoi = defaultdict(int)
    # for i, val in enumerate(gold_amounts):
    #     if (target - val) in vtoi:
    #         return [i, vtoi[target-val]]
    #     vtoi[val] = i
        
    for i, val in enumerate(gold_amounts):
        vtoi[val] = i
    for i, val in enumerate(gold_amounts):
        if (target - val) in vtoi:
            if vtoi[target - val] == i: continue
            return [i, vtoi[target-val]]
        
#problem 6
#U
    #input: [int] group_sizes
        #organize crew in groups 
        #pirate has ID from 0 to n-1
        #given int array group_sizes
            #group_sizes[i] is the size of the group pirate i shouldbe in
        #return list of groups so each pirate i is in group size group_sizes[i]
    #output: [[int]]
    #constraint: eahc pirate in 1 group, garunteed valid sol
    #edge:
#P
    #count -> list
    #merge all our values into 1 list

if __name__ == '__main__':
    # treasure_map1 = {
    #     "Cove": 3,
    #     "Beach": 7,
    #     "Forest": 5
    # }
    # print(total_treasure(treasure_map1))
    
    # message1 = "sphinx of black quartz judge my vow"
    # message2 = "trust me"
    # print(can_trust_message(message2))
    
    # chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
    # chests2 = [1, 1, 2]
    # print(find_duplicate_chests(chests1))
    # print(find_duplicate_chests(chests2))
    
    # code1 = "arghh"
    # code2 = "haha"
    # code3 = ""
    # print(can_make_balanced(code1)) 
    # print(can_make_balanced(code3)) 
    

    
    gold_amounts1 = [2, 7, 11, 15]
    target1 = 9
    gold_amounts2 = [3, 2, 4]
    target2 = 6
    gold_amounts3 = [3, 3]
    target3 = 6
    print(find_treasure_indices(gold_amounts1, target1))  
    print(find_treasure_indices(gold_amounts2, target2))  
    print(find_treasure_indices(gold_amounts3, target3)) 
    
    
