class Link(object):

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None



class LinkedList(object):

    def __init__(self):
        self.head = Link()
        self.tail = Link()
        self.head.next = self.tail
        self.tail.prev = self.head


    def first(self):
        return self.head.next

    def last(self):
        return self.tail.prev

    def empty(self):
        return self.head.next == self.tail

    def get(self, key):
        link = self.head

        while link != self.tail:
            if link.key == key:
                break
            link = link.next

        return link.val


    def include(self, key):
        link = self.head

        while link != self.tail:
            if link.key == key:
                return True
            link = link.next


        return False

    def append(self, key, val):
        old_prev = self.tail.prev

        new_link = Link(key, val)
        self.tail.prev = new_link
        new_link.next = self.tail
        new_link.prev = old_prev
        old_prev.next = new_link

    def update(self, key, val):
        link = self.head

        while link != self.tail:
            if link.key == key:
                break
            link = link.next

        if link != self.tail:
            link.val = val

        return link

    def remove(self, key):
        link = self.head

        while link != self.tail:
            if link.key == key:
                break

            link = link.next

        if link != self.tail:
            link.next.prev = link.prev
            link.prev.next = link.next

        return link
