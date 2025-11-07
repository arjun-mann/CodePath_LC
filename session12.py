#Understand:
    #input:
        #user has queue of songs
        #make Queue using a singly LL
        #queue is FIFO data struct
        #els are added to the end (the tail)
        #els are removed from head
    #output:
    #constraint:
#Plan:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        #initializes empty queue
    
    def is_empty(self):
        return True if not self.front else False
        
        #ret True, if empty, False otherwise
        #return if we have a node

    def enqueue(self, entry:tuple[str,str]):
        #Understand:
            #input: (str, str)
                #song, artist
                #adds element with specified tuple to end
            #output: NA
        #Plan
        #insert at the end
        if self.is_empty():
            self.front = Node(entry)
            self.rear = self.front
        else:
            self.rear.next = Node(entry)        # self.rear.next.value = entry
            self.rear = self.rear.next
    
    def dequeue(self):
        #Understand:
            #input: NA
                #remove el at front of queue
            #output: (str, str)
        #Plan:
        #remove a node at the front
        if self.is_empty():
             return None
        
        val = self.front.value
        self.front = self.front.next

        if not self.front:
             self.rear = None

        return val
                
    def peek(self):
        pass
        #Understand:
            #input: NA
            #output: (str, str)
            #constraint: if empty, return None
        #Plan:
        #return the val at the front, wihtout removing
        
        if not self.front:
            return None
        return self.front.value
        
    
# Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# View the front element
print("Peek: ", q.peek()) 

# Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty()) 

'''
Expected Output:
('Love Song', 'Sara Bareilles') -> ('Ballad of Big Nothing', 'Elliot Smith') 
-> ('Hug from a Dinosaur', 'Torres')
Peek:  ('Love Song', 'Sara Bareilles')
Dequeue:  ('Love Song', 'Sara Bareilles')
Dequeue:  ('Ballad of Big Nothing', 'Elliot Smith')
Is Empty:  False
Dequeue:  ('Hug from a Dinosaur', 'Torres')
Is Empty: True
'''


#problem 2:
#Understand:
    #input:
        #given head of 2 LL
            #playlist1, playlist2
        #lens n and m
        #remove playlist1's nodes from the ath to the bth node
        #put playlist2 in its place
    #output:
    #constraint:    #
#Plan:

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    #Understand:
        #input: node playlist1, node playlist2, int a, int b
            #replace inplace [a,b]
        #output: NA
        #constraint: a can be start of list, a == b, a < b, a and b will exist
    #Plan:
        #dummy node, start iterating until we hit a
        #do another count until we hit b
        #preva -> next with list2
        #list2's tail -> next = curr.next
        #O(N) time + O(1) mem
        
    #a: 1, b: 2
    #1 2 3 4
    #A B
    #1 A B 4
    
    dummy = Node(-1)
    dummy.next = playlist1
    curr = dummy #_ 1 2 3 4
    for i in range(a): #0 < 1 | 1 < 1
        curr = curr.next #curr = 1
    start = curr #start = 1
    for i in range(b-a+1): #2-1+1=2 | 0 < 2 | 1 < 2
        curr = curr.next #curr = 3
    start.next = playlist2 #1 A B
    curr2 = playlist2 #
    while curr2.next:
        curr2 = curr2.next
    curr2.next = curr.next #B 4
    return dummy.next
    

playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))

'''
Expected Output:
('Flea', 'St.Vincent') -> ('Juice', 'Lizzo') -> ('Dreams', 'Solange') -> ('First', 'Gallant')
-> ('Empty', 'Kevin Abstract')
'''

#problem 3:
#Understand:
    #input: node playlist
        #given head of LL playlist
        #shuffle 0 N 1 n-1 ...
    #ouput: node
    #constraint: empty node, case 1 node, no limits
#Plan:
    #1 2 3 4
    
    #1st pass:
    #stack: 3 4
    #1 4 2 3
    
    #first pass, get midpoint, push 2nd half nodes to stack
    #2nd pass, iterate until midpoint, alternate appending top el of stack
    #O(N) time + O(N) mem
    
    

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

from collections import deque
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def shuffle_playlist(playlist):
    my_stack = deque()
    fast = slow = playlist
    while fast.next and fast.next.next:
        slow = slow.next 
        fast = fast.next.next 
    midpoint = slow.next 
    slow = slow.next 

    while slow:
        my_stack.append(slow.val)
        slow = slow.next 
    
    dummy = Node(-1)
    cur1 = playlist

    while cur.val!=midpoint.val:
        dummy.next = cur1
        dummy.next.next = Node(my_stack.pop())
        cur1 = cur.next 
        
    return dummy.next


    