class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, new_node):
        if(self.head == None):
            self.head=new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node  #appending new node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def mid_node_del(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        mid = count//2
        temp = self.head
        n=0
        prev = None
        while temp and n < mid:
            prev = temp
            temp = temp.next
            n += 1
        prev.next = temp.next
list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.append(Node(50))
list.mid_node_del()
list.display()
