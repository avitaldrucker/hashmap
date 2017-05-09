class Link(object):

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def remove(self):
        prev_link = self.prev
        next_link = self.next
        prev_link.next = next_link
        next_link.prev = prev_link

    def __str__(self):
        return "[" + repr(self.key) + ", " + repr(self.val) + "]"
