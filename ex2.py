def move_to_front(n):
    lst = UnorderedList()
    for _ in range(n):
        s = input()
        if lst.search(s):
            lst.remove(s)
        lst.add(s)
    return lst