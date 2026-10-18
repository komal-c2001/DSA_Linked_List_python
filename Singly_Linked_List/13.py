
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        print("List Elements")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("None")

    def concatenate(self, other):
        if self.head is None:
            self.head = other.head
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = other.head


# First linked list
list1 = LinkedList()
list1.append(10)
list1.append(20)
list1.append(30)
list1.display()

# Second linked list
list2 = LinkedList()
list2.append(40)
list2.append(50)
list2.append(60)
list1.display()

# Concatenate
list1.concatenate(list2)

list1.display()
