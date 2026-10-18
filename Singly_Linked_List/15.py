class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class SinglyCircularLinkList:
    def __init__(self, head=None):
        self.head = head

    def insertAtPos(self, new_node, pos):
        if pos == 1:
            temp = self.head
            while (temp.next != self.head):
                temp = temp.next
            
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
        else:
            temp = self.head
            p = 1
            # Walk until temp is sitting at position pos - 1
            while p < pos - 1 and temp is not None:
                temp = temp.next
                p += 1
            
            if temp is not None:
                new_node.next = temp.next
                temp.next = new_node
    def append(self, new_node):
        if(self.head == None):
            self.head=new_node
            new_node.next = self.head
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node  #appending new node
            new_node.next = self.head
    

    def display(self):
        temp = self.head
        while True:
            print(temp.data ,end="->")
            temp = temp.next
            if temp == self.head:
                break
        print(temp.data)

# Test Run
obj = SinglyCircularLinkList()
obj.append(Node(10))   # [10]
obj.append(Node(20))   # [10, 20]
obj.append(Node(30))   # [10, 20, 30]

obj.insertAtPos(Node(100), 1)  # Insert 100 at pos 1 -> [100, 10, 20, 30]
obj.insertAtPos(Node(66), 4)   # Insert 66 at pos 4  -> [100, 10, 20, 66, 30]

obj.display()