# ......DELETION OPERATION......

# ......Delete Begin......

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

    def insert(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def del_begin(self):
        if self.head == None:
            print("Linked List is empty!")
        else:
            self.head=self.head.ref

    def del_end(self):
        if self.head == None:
            print("Linked List is empty!")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def del_by_value(self):
        if self.head == None:
            print("Linked List is empty!")
        else:
            pass


link=linkedlist()
link.insert(10)
link.insert(20)
link.insert(30)
link.insert(40)
link.insert(50)
link.del_begin()
link.del_end()
link.printLL()