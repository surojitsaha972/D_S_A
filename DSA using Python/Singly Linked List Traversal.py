# .............TRAVERSAL OPERATIONS..............
# Start with head of LL, Access tha data if head is not NULL. Go to Next node access node data, continue untill last node.

class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None

    def printLL(self):
        if self.head == None:
            print("Linked List is empty.")
        else:
            n=self.head
            while n!=None:
                print(n.data)
                n=n.ref

linkedlist().printLL()
