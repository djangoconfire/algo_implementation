# components of HashMap
#  array -> store the data
#  hash function - > convert key into index of hash map
#
class HashMap:
    def __init__(self):
        self.size=64
        self.map=[None] * self.size

    def _get_hash(self,key):
        hash=0
        for char in str(key):
            hash += ord(char)

        return hash % self.size

    def add(self,key,value):
        key_hash=self._get_hash(key)
        key_value=[key,value]

        if self.map[key_hash] is None:
            self.map[key_hash]=list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0]==key:
                    pair[1]=value
                    return True
            self.map[key_hash].append(key_value)
            return True


    def get_item(self,key):
        key_hash=self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]

        return None

    def delete_item(self,key):
        key_hash=self._get_hash(key)

        if self.map[key_hash] is None:
            return False

        for i in range(0,len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def print_item(self):
        print '<<<<<<<<<<<<<<<<------Final result ---------->>>>>>>>>'
        for item in self.map:
            if item is not None:
                print str(item)


h=HashMap()
h.add('Ritu',8602218669)
h.add('ranveer',9955418205)
h.add('sonam',7724915909)
h.add('sunny',8210445784)
h.add('katrina',8954145125)
h.add('hrithik',8602218669)


h.print_item()

