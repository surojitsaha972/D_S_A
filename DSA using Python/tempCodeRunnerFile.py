def printLL(self):
        if self.head == None:
            print("Linked List is empty!")
        else:
            n=self.head
            while n!=None:
                print(n.data)
                n=n.ref