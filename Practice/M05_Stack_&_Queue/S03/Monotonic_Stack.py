#1.Monotonic Increasing Stack
#General pattern
arr = [4,12,5,3,1,2,5,3,1,2,4,6]
stack = []
for x in arr:
    while stack and stack[-1] > x:
        stack.pop()
    stack.append(x)
#2.Monotonic Decreasing Stack
# #General pattern
stack = []
for x in arr:
    while stack and stack[-1] < x:
        stack.pop()
    stack.append(x)        
print(stack)    

#Next greater element
arr = [4,12,5,3,1,2,5,3,1,2,4,6]
NextGreaterElement = [-1]*len(arr)
stack = []
for i,x in enumerate(arr):
    while stack and arr[stack[-1]] < x:
        NextGreaterElement[stack.pop()] = x
    stack.append(i)

print(NextGreaterElement)    