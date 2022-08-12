import heapq

class PriorityQueue:
    def __init__(self):
            self._data = []
            self._index = 0
    def push(self, item, priority):
            heapq.heappush(self._data, (-priority, self._index, item))
            self._index += 1
    def pop(self):
            return heapq.heappop(self._data)[-1]

class Task:
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return f'{self.name}'
queue = PriorityQueue() # Create Priority queue
# Insert task in queue using push() method
queue.push(Task('daemon'), 23)
queue.push(Task('app'), 12)
queue.push(Task('os'),40)
queue.push(Task('service'),23)
# use pop() method to fetch element of highest priority
print(queue.pop()) # os
print(queue.pop()) # daemon
print(queue.pop()) # service
print(queue.pop()) # app            

def pop(self):
    return heapq.heappop(self._data)[-1]