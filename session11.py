#Understand:
    #input: node dna_strand, int m, int n
        #working on editing DNA
        #each node contains A, T, C, G
        #given head of LL, and 2 ints
            #write func to simulating selective deletion
        #start at beginning of DNA strand
            #retain first m nucletoides
            #remove the next n nucleotides
            #repeat until end of DNA strand reached
    #output:
        # head of the modified linked list
    #constraint:
    # edge cases: given head is None
#Plan:
    #count = 0
    
    #while True
        #iterate m nodes
            #if None, end early
            #return
        #store start
        #iterate n nodes
            #if None, end early
            #return
        #have start link to curr
        
    # dummy = Node()
    # dummy.next = curr
    # curr = dna_strand
    #while(curr):
        #for i in range(m):
            #curr = curr.next
            #if curr is None:
                #return dummy.next
        #stop = curr
        #for i in range(n):
            #curr = curr.next
            #if curr is None:
                #stop.next = None
                #return dummy.next
        #stop.next = curr
        
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    def edit_dna_sequence(dna_strand, m, n): #1 2 3 4 5 6 7 8 9 10
        dummy = Node() #N
        dummy.next = dna_strand #N 1 2 ...
        curr = dummy #N
        while(curr): #N
            for i in range(m): #0 1
                curr = curr.next #N 1 | N 1 2 
                if curr is None:
                    return dummy.next
            stop = curr #2
            for i in range(n): #N 1 2 | N 1 2 3 | N 1 2 3 4
                curr = curr.next #N 1 2 3 | N 1 2 3 4 | N 1 2 3 4 5
                if curr is None:
                    stop.next = None
                    return dummy.next
            stop.next = curr.next
        return dummy.next



#Understand:
    #input: node protein
        #each node represents amino acid
        #ret arr with values of any cycle in the list
            #LL has a cycle if at some point in the list
    #output: return an array with the values of any cycle in the list
    #constraint: 
    # edge cases: head is None
#Plan:
    # fast and slow pointers to get the start of the cycle
    # iterate through the cycle and store values in an array
# Implement:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    slow = protein
    fast = protein.next
    counter = 0
    while fast and fast != slow:
        fast = fast.next
        if counter % 2 == 0:
            slow = slow.next
        counter += 1
    if not fast:
        return []
    # iterate through the cycle
    result = [fast.value]
    node = fast.next
    while node != fast:
        result.append(node.value)
        node = node.next
    return result


protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))
        


