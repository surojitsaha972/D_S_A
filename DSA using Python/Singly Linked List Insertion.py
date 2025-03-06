# .............LINKED LIST............

# It is a linear data structures. It is a collection of nodes that are linked with each other. 
# A node contains two things first is data and second is a link that connects it with another node.
# Node: elements of linked lists.
# Advantages: Dynamic DS, Insertion & Deletion is easy, can implement stack queue & graph.
# Disadvantages: Needs extra memeory, Random access not possible
# Type: Singly Linked List, Doubly Linked List, Circular Linked List.

# ...............SINGLY LINKED LIST...............
# Operations: Inserting, Removing, Traversal

# .............INSERT OPERATIONS..............

# .....At the Begining.....

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

# .....At the Ending.....

    def ins_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            n.ref=new_node

# .....In_Between (After giving node).....   

    def after_node(self,data,x):
        n=self.head
        while n!=None:
            if x==n.data:
                break
            n=n.ref
        if n==None:
            print("Node is Empty in Linked List!")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref = new_node
            
      
# .....In_Between (Before giving node).....         




LL=linkedlist()
LL.ins_begin(10)
LL.ins_end(50)
LL.ins_begin(30)
LL.after_node(70,30)
LL.ins_begin(20)
LL.printLL()
