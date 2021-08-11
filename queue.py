class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def enqueue(self, elem):
        self.rear = self.rear + 1
        self.queue.append(elem)

    def dequeue(self):
        result = self.queue[self.front]
        self.queue.pop(self.front)
        return result

    def __str__(self):
        result = ''
        for item in self.queue:
            result += str(item) + ' '
        return result

    def getFront(self):
        return self.front

    def getRear(self):
        return self.rear

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.getFront())
print(queue.getRear())
print(queue)