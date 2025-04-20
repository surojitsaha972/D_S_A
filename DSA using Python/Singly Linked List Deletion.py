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

    def delete(self):
        if self.head == None:
            print("Linked List is empty!")
        else:
            self.head=self.head.ref

link=linkedlist()
link.insert(10)
link.insert(20)
link.insert(30)
link.delete()
link.printLL()