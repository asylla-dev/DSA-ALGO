class Node:
    def __init__(self, value):
        self.value = value;
        self.next = None
        self.length = 1

class LinkedList:
    def print_list(self, value):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def pop(self):
        if self.head is None:
            return None

        tmp = self.head
        pre = self.head

        while (tmp.next):
            pre = tmp
            tmp = tmp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        def prepend(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1
