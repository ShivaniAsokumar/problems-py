
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head == None:
            return -1
        if index > self.length - 1:
            return -1
        else:
            i = 0
            curr = self.head
            while i < index:
                curr = curr.next
                i += 1
            
            # We have reached the target index
            return curr.val

    def addAtHead(self, val: int):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        curr = Node(val)
        # List is empty
        if self.head == None:
            self.head = curr
            self.length += 1
        else:
            curr.next = self.head
            self.head = curr
            self.length += 1

    def addAtTail(self, val: int):
        """
        Append a node of value val to the last element of the linked list.
        """

        # List is empty
        curr = Node(val)
        if not self.head:
            self.head = curr
            self.length += 1
        else:
            # Iterate until we get to the last element in the list
            head_node = self.head
            while head_node.next:
                head_node = head_node.next
            
            head_node.next = curr
            self.length += 1
            
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node_to_add = Node(val)

        # Tail
        if index == self.length:
            self.addAtTail(val)
        # Head
        elif index == 0:
            self.addAtHead(val)
        elif index < self.length:
            head_node = self.head
            i = 0
            while i < index - 1:
                head_node = head_node.next
                i += 1
            next_node = head_node.next
            head_node.next = node_to_add
            node_to_add.next = next_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= 0 and index < self.length:
            self.length -= 1
            curr = self.head
            # Head Node
            if index == 0:
                self.head = self.head.next
            # Tail Node
            elif index == self.length - 1:
                i = 0
                while i < index - 1:
                    curr = curr.next
                    i += 1
                curr.next = None
                
            # Middle Node
            else:
                i = 0
                while i < index - 1:
                    curr = curr.next
                    i += 1
                curr.next = curr.next.next
                

    def printList(self):
        curr = self.head
        if not self.head:
            print('Empty List')
        else:
            while curr.next != None:
                print(curr.val, '->', end=' ')
                curr = curr.next
            print(curr.val, '->')


    

my_list = MyLinkedList()
my_list.addAtIndex(0,10)
my_list.printList()
my_list.addAtIndex(0,20)
my_list.printList()
my_list.addAtIndex(1,30)
my_list.printList()
print(my_list.get(0))





         


        




