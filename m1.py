def create_stack():
    return []
def push(name_stak,item):
    name_stak.append(item)
def empty_stack(name_stack):
    return len(name_stack) == 0
def pop(name_stack):
    return name_stack.pop()
i=0
stack1 = create_stack()
while i <= 10 :
    push(stack1,i)
    i=i+1

while  not empty_stack(stack1) :
    print(stack1[-1])
    pop(stack1)
