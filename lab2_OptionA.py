#Adrian Lopez, 09/16/19
#CS2302 - Data Structures
#Lab 2 option A

class Node(object):
    item = -1
    next = None

    def __init__(self, item):        
        self.item = item   
        self.next = None

class LinkedList: 
    #Function to initialize the Linked List object 
    def __init__(self):        
        self.head = None
        self.tail = None

    def append(self, item):        
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):        
        current_node = self.head
        while current_node is not None:
            print(current_node.item)
            # jump to the linked node
            current_node = current_node.next
        return
    def getCount(self): 
        temp = self.head # Initialise temp 
        count = 0 # Initialise count 
  
        # Loop while end of linked list is not reached 
        while (temp): 
            count += 1
            temp = temp.next
        return count

    # Solution 1
    def compareList(self):
        duplicate = 0
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            while next_node is not None:
                if int(current_node.item) == int(next_node.item):
                    duplicate += 1
                    break
                next_node = next_node.next
            current_node = current_node.next
        return duplicate

    # Solution 2       
    def bubbleSort(self):
        end = None
        while end != self.head:
            p = self.head
            while p.next != end:
                q = p.next
                if int(p.item) > int(q.item):
                    p.item, q.item = q.item, p.item
                p = p.next
            end = p

    # Solution 3
    # def merge(self):
    #     current_node = self.head
    #     while current_node is not None:
    #         next_node = current_node.next
    #         leftPos = current_node
    #         rightPos = next_node
    #         while leftPos.item <= rightPos and rightPos <= self.getCount():
    

    # Solution 4
    def checkDuplicates(self): 
        seen = [None] * 6001
        current_node = self.head
        while current_node is not None: 
            next_node = current_node.next
            if current_node.item == next_node.item: 
                for i in range(len(seen) - 1):
                    seen[i] == "True"
            else:
                for i in range(len(seen) - 1):
                    seen[i] == "False"
            current_node = current_node.next
        return seen
                


def main(): 
    #Create lists to store ID's
    listOne = []
    listTwo= []

    with open('downloads/vivendi.txt', 'r') as f:
        listOne = [line.strip() for line in f]
    with open('downloads/activision.txt', 'r') as f:
        listTwo= [line.strip() for line in f]

    #Combine both ID lists to one list; 6000 total
    joinedList = listTwo + listOne

    #Create new Linked list 
    myList = LinkedList()

    #Loop through list and add to linked list
    for i in joinedList:
        myList.append(i)

    print("Unsorted: ")
    myList.printList()
    print("Dupplicate: ", myList.compareList())
    myList.bubbleSort()
    print("Bubble Sort: ")
    myList.printList()
    print("Dupplicate: ", myList.compareList())

main()
