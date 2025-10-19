#Understand:
    #input: str name, str species, str catchphrase
        #define class with special method/function to create Villager
        #4 attributes in initialization
    #output:
    #constraint:
#Plan

VALID_LIST = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        self.personality = personality
        self.neighbor = neighbor
        
    def add_item(self, item_name):
        if item_name in VALID_LIST and item_name not in self.furniture:
            self.furniture.append(item_name) 

def of_personality_type(townies, personality_type):
    new_list = []
    for town in townies:
        if town.personality == personality_type:
            new_list.append(town.name)
    return new_list

#A -> B -> C -> NONE
#D
#curr: None

def message_received(start_villager, target_villager):
    curr = start_villager
    while curr != None:
        if curr == target_villager:
            return True
        curr = curr.neighbor
    return False
            
# if __name__ == '__main__':
    #problem 1:
    # apollo = Villager("Apollo", "Eagle", "pah")
    # print(apollo.name)
    # print(apollo.species) 
    # print(apollo.catchphrase)
    # print(apollo.furniture)
    
    #problem 2:
    # alice = Villager("Alice", "Koala", "guvnor")
    # print(alice.furniture)

    # alice.add_item("acoustic guitar")
    # print(alice.furniture)

    # alice.add_item("cacao tree")
    # print(alice.furniture)

    # alice.add_item("nintendo switch")
    # print(alice.furniture)

    #problem 3:
    # isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    # bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
    # stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

    # print(of_personality_type([isabelle, bob, stitches], "Lazy"))
    # print(of_personality_type([isabelle, bob, stitches], "Cranky"))
    
    #problem 4:
    # isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    # tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
    # kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
    # isabelle.neighbor = tom_nook
    # tom_nook.neighbor = kk_slider

    # print(message_received(isabelle, kk_slider))
    # print(message_received(kk_slider, isabelle))
    
    #problem 5:
    # print_linked_list(kk_slider)
    
    #problem 6:
    # fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
    # empty_list = None
    
    # print_linked_list(fish_list)
    # print_linked_list(catch_fish(fish_list))
    # print(catch_fish(empty_list))
    

#problem 2:
#Understand:
    #input:
        #create add_item()
        #takes 1 parameter item_name
            #if valid, add item_name to furniture
                #valid if has 1 of following values
    #output:
    #constraint:
#Plan:

#problem 3:
#Understand:
    #input: [Villager] townies, str personality_type
        #we added the attribute str personality
        #of_personality_type() is outside Villager
        #given a list of villager instances (townies), str personality type
            #return list of all names of villagers with matching personality
            #any order
    #output: [Villagers]
    #constraint:
#Plan:
    #we add personality to our class
    #create outside function to check personality types
        #if it's in match, include in our output, else skip
        
#problem 4:
#Understand:
    #input:
        #new attribute neighbor
            #none by default
        #write message_recieved()
            #ret True if you can pass a message from start to end villager
    #output: 
    #constraint:
#Plan:
    #neigbhor 

#problem 5:
#Understand:
    #input: Node(str)
    #output: Linked list(str)
    #constraint:
#Plan:


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle

#problem6
#Understand:
    #input:
        #LL for order of fish
        #head is next fish to catch
        #write catch_fish which accepts head
            #print name of fish in the head
            #remove first node from list
        #function should return the new head of the list
            #special message if empty
    #output:
    #constraint:
#Plan:
# print the head name
# move to the next

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head:
        print(f"I caught a {head.fish_name}!")
        head = head.next
        
    else:
        print("Aw! Better luck next time!")
        return None

if __name__ == '__main__':
    fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
    empty_list = None
    
    print_linked_list(fish_list)
    print_linked_list(catch_fish(fish_list))
    print(catch_fish(empty_list))


