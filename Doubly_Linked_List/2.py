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
    def insert (self,new_node,pos):
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head.prev = new_node 
            self.head = new_node
        else:
            p = 1
            while (p != pos-1):
                temp = temp.next
                p += 1
            new_node.prev = temp
            new_node.next = temp.next
            temp.next = new_node
            if temp.next:
                temp.next.prev = new_node
    def display(self):
        temp = self.head
        print("List Elements")
        while temp:
            print(temp.data,end="->")
            temp = temp.next

        print(self.head.data)

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.insert(Node(5),1)
list.insert(Node(50),6)
list.insert(Node(70),3)
list.display()
