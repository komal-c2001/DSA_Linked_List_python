
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next != None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def display(self):
        temp = self.head
        prev = None

        print("List Elements in Reverse Order")

        while temp:
            prev = temp
            temp = temp.next

        while prev:
            print(prev.data)
            prev = prev.prev

list = LinkedList()

list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))

list.display()
