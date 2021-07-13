from collections import deque
class queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(queue) > 0:
            return self.queue.popleft()
        else:
            return None
    def __str__(self):
        return str(self.queue)
#1 for enqueue, 2 for dequeue, 3 for print first item
def main(queue, queryType, item=None):
    if queryType == 1:
        endqi
