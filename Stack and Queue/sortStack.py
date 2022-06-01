import stack as st

stack1 = st.Stack()

stack1.push(16)
stack1.push(68)
stack1.push(34)
stack1.push(23)
stack1.push(75)
stack1.push(78)
stack1.push(23)
stack1.push(24)

def sortStack(stack):
    stack2 = st.Stack()
    while(not stack.isEmpty()):
        temp = stack.pop()
        while(not stack2.isEmpty() and stack2.peek() > temp):
            stack.push(stack2.pop())
        stack2.push(temp)
    while( not stack2.isEmpty()):
        stack.push(stack2.pop())
    return stack

sortStack(stack1)
stack1.print()