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

        def pop_first(self):
            if self.head is None:
                return None

            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return tmp

        def get(self, index):
            if index < 0 or index >= self.length:
                return None

            tmp = self.head
            for _ in range(index):
                tmp = tmp.next

            return tmp

        def set_value(self, index, value):
            if index < 0 or index >= self.length:
                return None
            tmp = self.get(index)
            if tmp is not None:
                tmp.value = value
                return True
            return False
