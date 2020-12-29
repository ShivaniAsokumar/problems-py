class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr = self.head

        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1
            curr = curr.next
        return total

    def display(self):
        elems = []
        curr = self.head
        while curr.next != None:
            curr = curr.next
            elems.append(curr.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print ("Error: Index out of range for 'Get'")
            return None
        curr_index = 0
        curr = self.head
        while True:
            curr = curr.next
            if curr_index == index: return curr.data
            curr_index += 1

    def delete(self, head, n):
        length = 0
        head = self.head
        node = head

        # Gets the length of the linked_list
        while node.next != None:
            length += 1
            node = node.next

        remove_index = length - n # Index of the node to be removed
        curr_node = self.head

        # When length = 1
        if length == 1:
            return curr_node
            
        # Tail node
        elif n == 1 and length > 1:
            i = 0
            while i < remove_index:
                curr_node = curr_node.next
                i += 1
            
            # Reached the second to last node
            curr_node.next = None

        # Head Node
        elif n == length:
            return curr_node

        # Vanilla Case (Middle Nodes)
        else:
            curr_node = self.head
            i = 0;
            while i < remove_index:
                curr_node = curr_node.next
                i += 1
            
            # Reached the node to remove
            curr_node.next = curr_node.next.next
            


        




my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.delete(my_list, 2)
my_list.display()

