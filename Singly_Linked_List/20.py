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
            while temp.next != None:
                temp = temp.next

            temp.next = new_node

        else:
            self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    # Add Two Numbers
    def subTwoNumbers(self, l1, l2):

        temp = Node(0)
        curr = temp

        while l1 or l2:
            sub = l1.data - l2.data
            l1 = l1.next
            l2 = l2.next
            curr.next = Node(sub)
            curr = curr.next
        self.head = temp.next
# First linked list
list1 = LinkedList()
list1.append(Node(6))
list1.append(Node(4))
list1.append(Node(3))

# Second linked list
list2 = LinkedList()
list2.append(Node(5))
list2.append(Node(6))
list2.append(Node(4))

# Addition
result = LinkedList()
result.subTwoNumbers(list1.head, list2.head)

print("First List:")
list1.display()

print("Second List:")
list2.display()

print("Substraction:")
result.display()