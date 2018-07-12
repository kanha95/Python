from collections import deque

ll = [5,3,2,1,7,9,8]

stack = deque(ll)

print stack.pop()
stack.append(11)
stack.append(13)

print stack

queue = deque(ll)

print queue.popleft()

queue.append(11)
queue.append(12)

print queue


