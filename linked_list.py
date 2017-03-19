class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


    def getData(self):
        return self.data

    def getLink(self):
        return self.next

    def setData(self,data):
        self.data=data

    def setLink(self,link):
        self.next=link



class UnorderedList:
    def __init__(self):
        self.head= None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp=Node(item)
        temp.setLink(self.head)
        self.head=temp

    def size(self):
        current=self.head
        count=0

        while current != None:
            count= count + 1
            current=current.getLink()

        return count


    def search(self,item):
        current=self.head
        found=False

        while current != None and not found:
            if current.getData() == item:
                found=True
            else:
                current = current.getLink()

        return found

    def remove(self,item):
        current=self.head
        previous=None
        found=False

        while not found:
            if current.getData() == item:
                found=True
            else:
                previous=current
                current=current.getLink()

            if previous == None:
                self.head= current.getLink()
            else:
                previous.setLink(current.getLink())


    def print_item(self):
        current=self.head
        linked_list = ""
        while current != None :
            linked_list += str(current.getData()) + '-->'
            current = current.getLink()

        print linked_list

list=UnorderedList()
list.add('ritu')
list.add(78)
list.add('katrina')
list.print_item()
print '@@@@@@@@@@@@@'
list.remove(78)
print list.size()
list.print_item()
list.add(45)
print list.search('ritu')
list.print_item()
