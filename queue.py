class Queue:
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return self.queue == []

    def enqueue(self,item):
        self.queue.insert(0,item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def print_item(self):
        if self.queue is not self.isEmpty():
            for item in self.queue:
                print item

q=Queue()
q.enqueue(45)
q.enqueue('ritu')
q.enqueue('457')
q.enqueue('raj')
q.print_item()
q.dequeue()
q.print_item()
print '@@@@@@@@@@@@@'
q.enqueue('katrina')
q.print_item()

