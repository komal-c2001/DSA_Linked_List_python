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
    def del_node(self, value):
        temp = self.head
        prev = None
        if(temp.data == value):
            self.head = self.head.next
            self.head.prev = None
            return
        else:   
            while(temp.data != value and temp):
                temp = temp.next
                if temp == None:
                    print("Value is not there in the list")
                    return
            temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
            temp = None    
    def display(self):
        temp = self.head
        print("List Elemennts")
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
list.del_node(40)
list.display()
