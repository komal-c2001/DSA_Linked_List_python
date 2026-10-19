class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, new_node):
        temp = self.head
        if temp:
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node  #appending new node
            new_node.prev = temp
        else:
            self.head = new_node
    def swap_First_Last(self):
        temp = self.head
        node1 = temp
        while temp.next:
            temp = temp.next
        temp.next = node1.next
        node1.next = None
        node1.prev = temp.prev
        temp.prev.next = node1
        temp.prev= None
        self.head = temp

    def display(self):
        temp = self.head
        print("List Elemennts")
        while temp:
            print(temp.data,end="->")
            temp = temp.next

list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.swap_First_Last()
list.display()
