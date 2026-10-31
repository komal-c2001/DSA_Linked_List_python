class Node:
    def __init__(self, data):
        self.data = data
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
            temp.next = new_node
    def isPalindrome(self):

        if self.head is None or self.head.next is None:
            return True

        # Find middle using slow and fast
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None

        while slow is not None:
            nextnode = slow.next
            slow.next = prev
            prev = slow
            slow = nextnode

        # Compare both halves
        temp1 = self.head

        while prev is not None:
            if temp1.data != prev.data:
                return False

            temp1 = temp1.next
            prev = prev.next
        return True
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.display()
print(list.isPalindrome())