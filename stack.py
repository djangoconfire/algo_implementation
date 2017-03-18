class Stack:
    def __init__(self):
    	self.stack=[]

    def is_empty(self):
    	return self.stack == []

    def pop(self):
    	return self.stack.pop()

    def peek(self):
    	return self.stack[len(self.stack)-1]

    def add(self,item):
    	self.stack.append(item)

    def size(self):
    	if self.stack is not self.is_empty():
    		return len(self.stack)
    	return None

    def print_item(self):
    	if self.stack is not self.is_empty():
    		for item in self.stack:
    			print item
s=Stack()
s.add(4)
s.add('golu')
s.add('ritu')
s.add('Bikki')
s.add('munna')
s.add(34)
print 'size of the stack is {}'.format(s.size())
print 'top of the stack is {}'.format(s.peek())
print 'removed elemnt is {}'.format(s.pop())
print 'size of the stack is {}'.format(s.size())
print '<<<<<,-----Stack Element------>>>>>>>'
s.print_item()
print 'top of the stack is {}'.format(s.peek())


