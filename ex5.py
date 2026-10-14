class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return current
            current = current.next
        return None

    def insert_front(self, item):
        new_node = DoubleNode(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_rear(self, item):
        new_node = DoubleNode(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_front(self):
        if self.is_empty():
            return None
        val = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return val

    def delete_rear(self):
        if self.is_empty():
            return None
        val = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return val

    def insert_before(self, node, item):
        if not node:
            return
        if node == self.head:
            self.insert_front(item)
        else:
            new_node = DoubleNode(item)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node

    def insert_after(self, node, item):
        if not node:
            return
        if node == self.tail:
            self.insert_rear(item)
        else:
            new_node = DoubleNode(item)
            new_node.next = node.next
            new_node.prev = node
            node.next.prev = new_node
            node.next = new_node

    def delete_node(self, node):
        if not node:
            return
        if node == self.head:
            self.delete_front()
        elif node == self.tail:
            self.delete_rear()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev