
from collections import Counter

#problem 1
#Understand
    #input: [int]
        #balanced = difference between min and max val == 1
        #return len of longest balanced subsequence
    #output: int
    #constraint: 
    #edge case: 
#Plan:
    #make freqmap
    #iterate it and do a running sum of curr key - prev key values
    
def find_balanced_subsequence(art_pieces):
    freqmap = Counter(art_pieces)
    maxlen = 0
    print(freqmap)
    for key, val in freqmap.items():
        if(key+1 in freqmap):
            maxlen = max(freqmap[key+1] + val, maxlen)
        if(key-1 in freqmap):
            maxlen = max(freqmap[key-1] + val, maxlen)
    return maxlen

#problem 2:
#Understand
    #input: [int]
        #valid if permuation of base[n]
        #base[n] defined as [1, 2, .., n-1, n, n]
        #arr of n+1 int from 1 to n-1
        #accepts array of art_pieces and returns T/F if authentic
    #output: T/F
    #constraint:
    #edge:
        #create freqmap for base[n]
        #create freqmap for input
        #return if equal
        
    #
        
def is_authentic_collection(art_pieces):
    inputfreq = Counter(art_pieces)  #[1, 3, 3, 2]
    print(inputfreq)
    for k, v in inputfreq.items(): #({3: 2, 1: 1, 2: 1})
        if k == len(inputfreq):
            if v != 2:
                return False
        elif k > len(inputfreq) or k < 0:
            return False
        elif v != 1:
            return False
    return True

#problem 3
#Understand
    #input: [int] 
        #list of strings collection
        #display prints in 2D
        #conditions
            #only contain elements in collection
            #each row only has distinct strings
            #num of rows should be minimal
        #return resulting array
    #output: 
        # [[int]]
    #constraint: any valid answer
    #edge: 
#Plan
    #approach 1: create a frequency map
    #freqmap
    #gallary = [] (2d list)
    #count = len(freqmap)
    #while count > 0
        #row = []
        #for k, v in map
            #if v > 0: row.append(k)
            #map[k] -= 1
            #if map[k] == 0: count -= 1
        #gallary.append(row)
    #return gallary
    
    
    #approach 2: set for each row
    
def organize_exhibition(collection):
    freqmap = Counter(collection)
    gallary = [] #(2d list)
    count = len(freqmap)
    while count > 0:
        row = []
        for k, v in freqmap.items():
            if v > 0: row.append(k)
            freqmap[k] -= 1
            if freqmap[k] == 0: count -= 1
        gallary.append(row)
    return gallary
        
#problem 4
#Understand
    #input: [str]
        #virtual gallary's traffic tracked through domain names
        #each domain has subdomains
        #modetern.artmuseum.com
            #top: com
            #next: artmuseum.com
            #last: modern.artmuseum.com
        #count-paired domain: "rep d1.d2.d3"
        #rep is num of visits to domain and d1.d2.d3 is domain
        #9001 domain -> domain visited 9001 times
        #given: arry of count-paired domains
        #return arr of count-paired domains of each subdomain
    #output: [str]
    #constraint: empty
    #edge: empty
#Plan
    #for domin in cpdomains:
        #for len of num periods in domain
            #split from last period
            #map[substr] += 1
    #iterate our map
        #result.append(v + " " + k)
    
def subdomain_visits(cpdomains):
    freqmap = defaultdict(int)
    for domain in cpdomains:
        visits, words = domain.split()
        subdomains = words.split('.')
        for i in range(len(subdomains)-1, -1, -1):
            running += subdomains[i]
            freqmap[running] += visits
            running = "." + running
    return [f'{val} {key}' for key, val in freqmap.items()]
        
            
        
    
if __name__ == '__main__':
    #p 1
    # art_pieces1 = [1,3,2,2,5,2,3,7]
    # art_pieces2 = [1,2,3,4]
    # art_pieces3 = [1,1,1,1]

    # print(find_balanced_subsequence(art_pieces1))
    # print(find_balanced_subsequence(art_pieces2))
    # print(find_balanced_subsequence(art_pieces3))
    
    #p 2
    # collection1 = [2, 1, 3]
    # collection2 = [1, 3, 3, 2]
    # collection3 = [1, 1]

    # print(is_authentic_collection(collection1))
    # print(is_authentic_collection(collection2))
    # print(is_authentic_collection(collection3))
        
    #p 3
    collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
    collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

    print(organize_exhibition(collection1))
    print(organize_exhibition(collection2))