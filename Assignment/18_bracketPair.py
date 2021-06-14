seq = input()

stack = []
for ch in seq:
    if(ch=='('):
        stack.append('x')
    elif(ch==')'):
        if(stack):
            stack.pop()
        else:
            stack.append('x')
            break

if(stack):
    print("invalid sequence")
else:
    print("No errors")