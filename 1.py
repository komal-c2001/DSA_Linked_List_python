class Node:
    def __init__(self, val):
        self.prev = None
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
    def display(self):
        temp = self.head
        print("List Elements")
        while temp:
            print(temp.data,end="->")
            temp = temp.next

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))

list.display()
