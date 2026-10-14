class StackUL:
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop(0)


class QueueUL:
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


class DequeUL:
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def add_front(self, item):
        self.items.add(item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()


import time


def run_performance_experiment():
    n = 2000

    start = time.time()
    py_queue = []
    for i in range(n):
        py_queue.append(i)
    for i in range(n):
        py_queue.pop(0)
    t_py = time.time() - start

    ul_queue = QueueUL()
    start = time.time()
    for i in range(n):
        ul_queue.enqueue(i)
    for i in range(n):
        ul_queue.dequeue()
    t_ul = time.time() - start

    print("Время работы очереди на встроенных списках:", t_py)
    print("Время работы очереди на связном списке:", t_ul)