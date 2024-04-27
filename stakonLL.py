# class stack:
#     def __init__(self,l):
#         self.stack_list=[]
#         self.limit=l
    
#     def push_method(self,val):
#          if(len(self.stack_list) <= self.limit):
#           self.stack_list.append(val)
#          else:
#               print("stack over flow")

#     def pop_method(self,val):
#         if(len(self.stack_list)<= self.limit):
#             self.stack_list.pop(val)
#         else:
#             print("stack under flow")

# stack_1 = stack(5)
# stack_2 = stack(3)
# stack_1.push_method(8)



# class stack:
#     def __init__(self, l):
#         self.stack_list = []
#         self.limit = l
    
#     def push_method(self, val):
#         if (len(self.stack_list) < self.limit):
#             self.stack_list.append(val)
#         else:
#             print("Stack overflow")

#     def pop_method(self, val): 
#         if (len(self.stack_list) > 0): 
#             self.stack_list.pop(val)  
#         else:
#             print("Stack underflow")

# stack_1 = stack(5)
# stack_2 = stack(3)
# stack_1.push_method(8)


class Stack:
    def __init__(self, limit):
        self.stack_list = []
        self.limit = limit
    
    def push_method(self, val):
        if(len(self.stack_list) < self.limit):
            self.stack_list.append(val)
        else:
            print("Stack overflow")

    def pop_method(self): 
        if(len(self.stack_list) > 0): 
            return self.stack_list.pop()  
        else:
            print("Stack underflow")

stack_1 = Stack(5)
stack_2 = Stack(3)


stack_1.push_method(8)
stack_1.push_method(10)
stack_1.push_method(15)


pop_value = stack_1.pop_method()
print("pop val stack_1:", pop_value)


stack_1.push_method(20)
stack_1.push_method(25)


stack_1.push_method(30)


while True:
    pop_value = stack_1.pop_method()
    if pop_value is None:
        break
    print("Popped value from stack_1:", pop_value)

stack_1.pop_method()
