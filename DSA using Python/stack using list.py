# LIFO(Last In First Out) or FILO(First In Last Out)
# Ex.: Pline of books,stack of dinner plates etc.

# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# print(stack)
# print(stack[-1])
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)

stack=[]
def push():
    ele=int(input("Enter the element: "))
    stack.append(ele)
    print(stack)

def pop():
    if stack==[]:
        print("Empty stack.")
    else:
        elem=stack.pop()
        print("Removed element from the stack is ",elem)
        print(stack)
while True:
    print("Select the operation 1.Push 2.Pop 3. Quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter the correct option.")
