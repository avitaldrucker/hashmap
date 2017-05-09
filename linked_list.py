from link import Link


class LinkedList(object):


    def __init__(self):
        self.head = Link()
        self.tail = Link()
        self.head.next = self.tail
        self.tail.prev = self.head


    def __getitem__(self, desired_index):
        current_index = 0
        link = self.first()
        while link != self.tail:
            if current_index == desired_index:
               return link
            link = link.next
            current_index += 1

        return None


    def first(self):
        return self.head.next


    def last(self):
        return self.tail.prev


    def empty(self):
        return self.first() == self.tail


    def get(self, key):
        link = self.first()

        while link != self.tail:
            if link.key == key:
                return link.val
            link = link.next

        return None


    def include(self, key):
        return not not self.find(key)


    def append(self, key, val):
        old_prev = self.tail.prev

        new_link = Link(key, val)

        new_link.next = self.tail
        self.tail.prev = new_link

        new_link.prev = old_prev
        old_prev.next = new_link


    def find(self, key):
        link = self.first()

        while link != self.tail:
            if link.key == key:
                return link
            link = link.next

        return None


    def update(self, key, val):
        link = self.find(key)
        if link:
            link.val = val

        return link


    def remove(self, key):
        link = self.find(key)
        if link:
            link.remove()

        return link


    def __str__(self):
        links = []
        link = self.first()

        while link != self.tail:
            links.append(str(link))
            link = link.next

        return ", ".join(links)
