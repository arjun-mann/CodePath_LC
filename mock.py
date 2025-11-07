#Understand:
    #input:
        #2 non-empty LL
            #2 non negative integers
            #digits stored in reverse order
            #each ndoe contains a single digit
            #add the two numbers and return the sum as a linked list
            #no leading 0's
    #output: linked list
    #constraint: no leading 0's
#Plan:

# 1 2 3
# 4 5 6
# 5 7 9

#9 9 9
#2 2 2
#1 2 2 1

#9
#9 9
#8 0 1

#321 + 654 = 975
#9 7 5
#5 7 9

#iterate l1 and l2
    #sum up the values, store in my new list
    #carry will be updated
#iterate l1
    #sum up l1 val and carry
    #carry will be updated
#same for l2

class Node(val=0, next=None):
    self.val = val
    self.next = None

def addTwoNumbers(list1 : Node, list2 : Node):
    dummy = Node()
    curr = dummy
    carry = 0
    while list1 and list2:
        curr.next = Node(list1.val + list2.val + carry)
        carry = (list1.val + list2.val + carry) // 10
        list1 = list1.next
        list2 = list2.next
    while list1:
        curr.next = Node(list1.val + carry)
        carry = (list1.val + carry) // 10
        list1 = list1.next
    while list2:
        curr.next = Node(list1.val + carry)
        carry = (list1.val + carry) // 10
        list2 = list2.next
    return dummy.next()

if __name__ == '__main__':
    l1 = Node(5, Node(6, Node(4)))
    l2 = Node(7, Node(0, Node(8)))
    res = addTwoNumbers(l1, l2)
    while res:
        print(f'{res.val} -> ')

    

    
