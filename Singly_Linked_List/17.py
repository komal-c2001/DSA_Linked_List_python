class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,newnode):
        if(self.head == None):
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
    def insertAtPos(self,newnode,pos):
        if(pos == 1):
            self.head.next = self.head
            self.head = newnode
        else:
            p = 1
            temp = self.head
            while p < pos - 1 and temp is not None:
                temp = temp.next 
                p += 1
            if temp is not None:
                newnode.next = temp.next
                temp.next = newnode
    def reverse(self):
        temp = self.head
        prev = None
        while temp:
            nextnode = temp.next
            temp.next = prev
            prev = temp 
            temp = nextnode
        self.head = prev
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.insertAtPos(Node(50),5)
list.reverse()
list.display()