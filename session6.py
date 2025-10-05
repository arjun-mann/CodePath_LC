

#Understand:
    #input: [int] blueprints
        #in charge of overseeing blueprint approval for architectural designs
        #each blueprint has a complexity level
            #represented by int
        #approval process:
            #blueprints with lower complexity come first
            #if a higher complexity is submitted, it must wait until simpler have been approved
        #simulate using queue
        #return order blueprints are approved
    #output: return order processed
    #constraint: 
    #edge: empty
#Plan:
    #


from collections import deque
def blueprint_approval(blueprints):
    queue = deque()
    for i in sorted(blueprints):
        queue.append(i)
    res = []
    while queue:
        res.append(queue.popleft())
    return res


    
#problem 2:

#Case 1:
#10 5 8 3 7 2 9
#10 [5, 8] [3, 7] [2, 9]


#Understand:
    #input: [int] floors
        #given [int] floors
        #rep heights of building floors
        #task is to design a skyscraper
            #each floor must be on a floor with >= height
        #only start a new skyscraper when necessary
            #no more floors can be added according to rules
        #return num of skyscrapers built
    #output: int
    #constraint:
    #edge: 0 buildings
#Plan
    #track previous
    #previous = float('-inf')
    #count = 0
    #iterate list: 0, end
        #if our curr >= previous
            #count += 1
        #previous = curr
    #return count
    
    #8, 6, 4, 7, 5, 3, 2
    #[8], [6], [4, 7], [5], [3], [2]
    
    # 8, 6, 4, 4, 7, 5, 3, 2
    #
    
def build_skyscrapers(floors): #8, 6, 4, 7, 5, 3, 2
    previous = float('-inf') #
    skyscraper_count = 0 #
    for height in floors: #8, 6, 4
        if height > previous: 
            skyscraper_count += 1 #2
        previous = height #6
    return skyscraper_count


if __name__ == '__main__':
    # print(blueprint_approval([3, 5, 2, 1, 4])) 
    # print(blueprint_approval([7, 4, 6, 2, 5])) 
    
    print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
    print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
    print(build_skyscrapers([8, 6, 4, 4, 7, 5, 3, 2])) 
    

#problem 3:
#Understand:
    #input: [int]
        #designing a corridor
        #corridor is a list of int, each val is width of segment
        #find 2 segments such that corridor between has max possible area
        #area is defined as minimum width of 2 segments, multiplied by distance
    #output: area = min(width1, width2) * distance between their indices (height)
    #constraint:
    #edge:
#Plan


    left = 0
    maxvol = 0
    right = len(segments) - 1
    while (left < right):
        maxvol = max(maxvol, (right-left) * min(left, right))
        if left < right:
            left += 1
        else:
            right -= 1
        
        

        