class Deque:
    def __init__(self):
        self.deque=[]

    def isEmpty(self):
        return self.deque == []

    def addFront(self,item):
        self.deque.append(item)

    def addRear(self,item):
        self.deque.insert(0,item)

    def removeFront(self):
        return self.deque.pop()

    def removeRear(self):
        return self.deque.pop(0)

    def size(self):
        return len(self.deque)

    def print_item(self):
        if self.deque is not self.isEmpty():
            for item in self.deque:
                print item



d=Deque()
print d.print_item()
print '@@@@@@@@@@@@@@@@'
d.addFront(45)
d.addRear('ritu')
d.addRear('monu')
print d.print_item()
d.removeRear()
d.print_item()
print '################'
