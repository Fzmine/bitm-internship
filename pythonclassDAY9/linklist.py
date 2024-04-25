

# class node:
#     def __init__(self, d):
#         self.data = d
#         self.next = None

# class LL:
#     def __init__(self):
#          self.head = None
    
#     def add_node(self, val):
#         new_node = node(val)
#         if self.head == None:
#             self.head = new_node
#         else:
#             traveller = self.head
#             while(traveller.next != None):
#                 traveller = traveller.next
#             traveller.next = new_node
    
#     def traverse(self):
#         traveller = self.head
#         while(traveller != None):
#             print(traveller.data)
#             traveller = traveller.next
        
    
#     def delete_node(self):
#         traveller = self.head
#         prev = self.head
#         while(traveller.next != val):
#           prev = traveller
#           traveller = traveller.next
#         if traveller is None:
#             print("Node with value", val )
#             return
        
        
        

#     def delete_at_start(self):
#         self.head=self.head.next

#     def add_node_at_start(self):
#         new_node = node(2)
#         temp = self.head
#         self.head = new_node
#         self.head.next = temp

        
# LL1 = LL()
# LL1.add_node(3)
# LL1.add_node(8)
# LL1.add_node(6)
# LL1.add_node(1)
# LL1.delete_at_start()
# LL1.add_node_at_start()

# LL1.traverse()  

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
            while traveller.next != None:
                traveller = traveller.next
            traveller.next = new_node
    
    def traverse(self):
        traveller = self.head
        while traveller != None:
            print(traveller.data)
            traveller = traveller.next
        
    
    def delete_node(self, val):
        traveller = self.head
        prev = None
        # If the node to be deleted is the head node
        if traveller is not None and traveller.data == val:
            self.head = traveller.next
            traveller = None
            return
        # Find the node to be deleted
        while traveller is not None and traveller.data != val:
            prev = traveller
            traveller = traveller.next
        # If the node is not found
        if traveller is None:
            print("Node with value", val, "not found.")
            return
        # Delete the node
        prev.next = traveller.next
        traveller = None

    def delete_at_start(self):
        if self.head is not None:
            self.head = self.head.next

    def add_node_at_start(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

# Create a linked list instance
LL1 = LL()
# Add some nodes
LL1.add_node(3)
LL1.add_node(8)
LL1.add_node(6)
LL1.add_node(1)

# Demonstrate traversing the original list
print("Original linked list:")
LL1.traverse()  

# Demonstrate deleting the first node and adding a node at the start
LL1.delete_at_start()
LL1.add_node_at_start(2)

# Demonstrate traversing the modified list
print("\nLinked list after deleting at start and adding at start:")
LL1.traverse()
