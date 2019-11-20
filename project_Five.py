#Create on 11/12/19 by: Adrian Lopez 
#Project 5; Data Structures 2302, Instructor: Diego Aguirre, T.A: Gerardo Barraza
#Purpose (Problem A): implement a data structure called Least Recently Used (LRU) cache. 

class Node: 
    def __init__(self, data): 
        self.next = None 
        self.prev = None
        self.data = data 

class LRUCache:
    def __init__(self, capacity, head=None, tail=None):
        self.capacity = capacity
        self.hash = {}
        self.head = head    
        self.tail = tail 

    def get_key(self, key):
        if key in self.hash:
            val = self.hash[key]
            return val.data
        return -1

        # if key not in self.hash:
        #     return -1
        # v = self.hash.pop(key) 
        # self.hash[key] = v  
        # return v

    def put_key(self, key, value):
        n = Node(value)
        self._add(n)
        self.hash[key] = n

        if key in self.hash:
            self.hash.pop(key)

        if len(self.hash) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.hash[n.key]
    
    def size(self):

        return len(self.hash)
    
    def max_capacity(self):
        
        return self.capacity

    def _remove(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev
    
    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail

class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def most_frequent(self, word_list):
        if word_list is None:
            print("EMPTY")
            return
        
        for words in word_list:
            #NEEDS TO BE FINISHED
            return 

    

def main():

    cache = LRUCache(3)
    cache.put_key(1, 5)
    print(cache.get_key(1))

    main()


