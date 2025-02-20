# .............LINKED LIST............

# It is a linear data structures. It is a collection of nodes that are linked with each other. 
# A node contains two things first is data and second is a link that connects it with another node.
# Node: elements of linked lists.
# Advantages: Dynamic DS, Insertion & Deletion is easy, can implement stack queue & graph.
# Disadvantages: Needs extra memeory, Random access not possible
# Type: Singly Linked List, Doubly Linked List, Circular Linked List.

# ...............SINGLY LINKED LIST.............
# Operations: Inserting, Removing, Traversal


# .............TRAVERSAL OPERATIONS..............
# Start with head of LL, Access tha data if head is not NULL. Go to Next node access node data, continue untill last node.

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
# class linkedlist:
#     def __init__(self):
#         self.head=None

#     def printLL(self):
#         if self.head == None:
#             print("Linked List is empty.")
#         else:
#             n=self.head
#             while n!=None:
#                 print(n.data)
#                 n=n.ref

# linkedlist().printLL()


# .............INSERT OPERATIONS..............

# ...At the Begining...

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None

    def printLL(self):
        if self.head == None:
            print("Linked List is empty!")
        else:
            n=self.head
            while n!=None:
                print(n.data)
                n=n.ref
    
    def ins_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

LL=linkedlist()
LL.ins_begin(10)
LL.ins_begin(20)
LL.ins_begin(30)
LL.printLL()

# ...At the Ending...

