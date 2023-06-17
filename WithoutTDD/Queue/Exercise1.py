import random
import time
import string
from collections import deque

queue = deque()

def addClient(queue):
    queue.append(random.choice(string.ascii_letters))
    print("The client:", queue[-1], "has been added to the queue")

def attendClient(queue):
    if len(queue) > 0:
        print("The client:", queue[0], "has been attended")
        queue.popleft()

while True:
    if random.random() < 0.5:
        addClient(queue)
    
    if len(queue) > 0:
        attendClient(queue)

    time.sleep(2)
