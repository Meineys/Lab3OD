class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next

    def append(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = temp

    def index(self, item):
        current = self.head
        idx = 0
        while current is not None:
            if current.data == item:
                return idx
            current = current.next
            idx += 1
        raise ValueError()

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
            return
        current = self.head
        previous = None
        idx = 0
        while current is not None and idx < pos:
            previous = current
            current = current.next
            idx += 1
        temp = Node(item)
        previous.next = temp
        temp.next = current

    def pop(self, pos=-1):
        if self.head is None:
            raise IndexError()
        if pos == -1:
            current = self.head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            if previous is None:
                self.head = None
            else:
                previous.next = None
            return current.data
        else:
            current = self.head
            previous = None
            idx = 0
            while current is not None and idx < pos:
                previous = current
                current = current.next
                idx += 1
            if current is None:
                raise IndexError()
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
            return current.data

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(repr(current.data))
            current = current.next
        return "[" + ", ".join(result) + "]"

    def slice(self, start, stop):
        new_list = UnorderedList()
        current = self.head
        idx = 0
        elements = []
        while current is not None and idx < stop:
            if idx >= start:
                elements.append(current.data)
            current = current.next
            idx += 1
        for el in reversed(elements):
            new_list.add(el)
        return new_list