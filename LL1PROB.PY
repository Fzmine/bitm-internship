class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    
    def add_node(self, val):
        new_node = Node(val)
        if(self.head is None):
            self.head = new_node
        else:
            traveller = self.head
            while(traveller.next is not None):
                traveller = traveller.next
            traveller.next = new_node
    
    def traverse(self):
        traveller = self.head
        while(traveller is not None):
            print(traveller.data)
            traveller = traveller.next
        
    def delete_node(self, val):
        traveller = self.head
        prev = None
        if (traveller is not None and traveller.data == val):
            self.head = traveller.next
            traveller = None
            return
        
        while(traveller is not None and traveller.data != val):
            prev = traveller
            traveller = traveller.next
            
        if(traveller is None):
            print("Node with value", val)
            return
        
        prev.next = traveller.next
        traveller = None


def merge_sorted_lists(ll1, ll2):
    merged_ll = LL()
    traveller1 = ll1.head
    traveller2 = ll2.head
    
    while(traveller1 is not None or traveller2 is not None):
        if(traveller1 is None):
            merged_ll.add_node(traveller2.data)
            traveller2 =traveller2.next
        elif(traveller2 is None):
            merged_ll.add_node(traveller1.data)
            traveller1 =traveller1.next
        elif(traveller1.data <traveller2.data):
            merged_ll.add_node(traveller1.data)
            traveller1 =traveller1.next
        else:
            merged_ll.add_node(traveller2.data)
            traveller2 =traveller2.next
    
    return merged_ll

LL1 = LL()
LL1.add_node(1)
LL1.add_node(5)
LL1.add_node(10)

print("LL1:")
LL1.traverse()  

LL2 = LL()
LL2.add_node(2)
LL2.add_node(7)
LL2.add_node(13)

print("LL2:")
LL2.traverse()


merged_ll = merge_sorted_lists(LL1, LL2)
print("Merged List: ")
merged_ll.traverse()
