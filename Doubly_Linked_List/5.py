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
    def count_occurence(self,num):
        count = 0
        temp = self.head
        while temp:
            if(temp.data == num):
                count += 1
            temp = temp.next
        print("Count of ",num,"=",count)


    def display(self):
        temp = self.head
        print("List Elemennts")
        while temp:
            print(temp.data,end="->")
            temp = temp.next

list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(10))
list.append(Node(30))
list.append(Node(40))
list.append(Node(10))
list.count_occurence(10)
list.display()
