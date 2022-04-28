import sys
input = sys.stdin.readline

tokens = input().rstrip()
op = []
stack = []

priority = {'*':2,'/':2,'+':1,'-':1,'(':0}
for i in tokens:
    if i.isalpha():
        op.append(i)
    elif i == '(':
            stack.append(i)
    elif i == ')': 
        while stack[-1] != '(':
            op.append(stack.pop())
        stack.pop()
    else:
        #  i이 stack[-1]의 우선순위와 같거나 보다 작으면
        #  i의 우선순위가 더 커질때까지 pop
        while stack and priority[i] <= priority[stack[-1]]:
            op.append(stack.pop())  
        stack.append(i)

while len(stack) != 0:
    op.append(stack.pop())
    
print(''.join(op))