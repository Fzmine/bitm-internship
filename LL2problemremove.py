class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    
    def add_node(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            traveller = self.head
            while(traveller.next != None):
                traveller = traveller.next
            traveller.next = new_node
    
    def traverse(self):
        traveller = self.head
        while(traveller != None):
            print(traveller.data)
            traveller = traveller.next
    
    def delete_third_node(self):
        traveller = self.head
        prev = None
        count = 1
        while(traveller != None and count < 3):
            prev = traveller
            traveller = traveller.next
            count += 1
        
        if(traveller is None):
            print("There are less than three nodes in the list.")
            return
        
        
        if(traveller.next is not None):
            prev.next = traveller.next
        else:
            prev.next = None

LL1 = LL()
LL1.add_node(3)
LL1.add_node(8)
LL1.add_node(6)
LL1.add_node(1)

LL1.traverse()


LL1.delete_third_node()

print("LL after deleting the third node:")

LL1.traverse()
