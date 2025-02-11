# FIFO(First In First Out) & LILO(Last In Last Out)
# In queue, Process to add element is called ENQUEUE and remove element is called DEQUEUE.
# Ex.: Customer service, banking etc.

queue=[]
def enq():
    ele=int(input("Enter a number: "))
    queue.append(ele)
    print(ele, "is added to queue")
def deq():
    if not queue:
        print("Queue is empty!!")
    else:
        ele=queue.pop(0)
        print("Removing Element is: ",ele)
def display():
    print(queue)

while True:
    print("Select the operations 1.Add 2.Remove 3.show 4.quit")
    ch=int(input())
    if ch==1:
        enq()
    elif ch==2:
        deq()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("Please engter the correct operation.")