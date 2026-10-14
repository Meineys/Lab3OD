class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

import re

def check_html(html_string):
    tags = re.findall(r'<\s*(/?\w+)[^>]*>', html_string)
    stack = Stack()
    for tag in tags:
        if not tag.startswith('/'):
            stack.push(tag)
        else:
            if stack.is_empty():
                return False
            if stack.pop() != tag[1:]:
                return False
    return stack.is_empty()