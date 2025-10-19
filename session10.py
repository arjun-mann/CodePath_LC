#problem 1
#Understand:
    #input: head of LL
        #ret maxval in LL
        #assume the LL contains only numeric value
    #output: int
    #constraint:
#Plan:
"""
Problem 1: Greatest Node
Write a function find_max() that takes in the head of a linked list and returns the maximum value in the linked list. You can assume the linked list will contain only numeric values.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    if head is None:
        return None
    # max = head.value
    # curr = head
    
    # while curr:
    #     max = max(curr.val, maxval)
    #     curr = curr.next
        
    curr = head
    maxval = float('-inf')
    while curr:
        maxval = max(curr.value, maxval)
        curr = curr.next
    return maxval


#problem 2:
#Understand:
    #input:
        #implements remove_tail()
            #accepts head of a LL
            #removes last ndoe of list
            #return head of modified list
    #output: head
    #constraint:
#Plan:
    

"""
Problem 2: Remove Tail
The following code incorrectly implements the function remove_tail(). When correctly implemented, remove_tail() accepts the head of a singly linked list and removes the last node (the tail) in the list. The function should return the head of the modified list.

Step 1: Copy this code into your IDE.

Step 2: Create your own test cases to run the code against. Use print statements, print_linked_list(), and the stack trace to identify and fix any bugs so that the function correctly removes the last node from the list.
"""

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

def remove_tail(head):
    
    if head is None or head.next is None:
        return None
    
    
    #A B
    current = head #A
    while current.next.next: #None
        current = current.next

    current.next = None #A -> None
    return head #A

#problem 3:
#Understand:
    #input: head
        #given head of sorted LL
        #delete alements that occur more than once
        #the resulting list should maintain sorted order
        #return the head of the linked list
    #output:
    #constraint:
#Plan:

    #1 2 3 3 4 5
    #prev: None
    #curr: 1

    prevprev = None
    prev = None 
    curr = head
    while curr: 
        if prev and prev.value == curr.value: #False | False | False | True  | False
            while curr and prev.value == curr.value: #3 == 3 | False
                curr = curr.next # 4
            prevprev.next = curr #3 -> 4
        prevprev = prev
        prev = curr 
        curr = curr.next 
    return head
    

"""
Problem 3: Delete Duplicates in a Linked List
Given the head of a sorted linked list, delete all elements that occur more than once in the list (not just the duplicates). The resulting list should maintain sorted order. Return the head of the linked list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

#1 1 2
def delete_dupes(head):
    dummy = Node()
    dummy.next = head
    prevprev = None
    curr = dummy

    "dummy -> 1 -> 1 -> 2 -> 3 -> 3 -> 4"
    
    while curr: 
        if prev and prev.value == curr.value: #False | False | False | True  | False
            while curr and prev.value == curr.value: #3 == 3 | False
                curr = curr.next # 4
            prevprev.next = curr #3 -> 4
        prevprev = prev
        prev = curr 
        curr = curr.next 
        
    return dummy.next

if __name__ == '__main__':
    #problem 1
    # head1 = Node(5, Node(6, Node(7, Node(8))))

    # # Linked List: 5 -> 6 -> 7 -> 8
    # print(find_max(head1))

    # head2 = Node(5, Node(8, Node(6, Node(7))))

    # # Linked List: 5 -> 8 -> 6 -> 7
    # print(find_max(head2))
    
    #problem 2
    # head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

    # # Linked List: Isabelle -> Alfonso -> Cyd
    # print_linked_list(remove_tail(head))
    
    #problem 3
    head = Node(1, Node(1, Node(2, Node(3, Node(3, Node(4, Node(5)))))))

    # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
    print_linked_list(delete_dupes(head))

    
    