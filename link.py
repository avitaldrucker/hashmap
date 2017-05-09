class Link(object):


    # Initialize new Link object - default parameters for key and value
    # are None
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


    # Excises the link from a linked list by changing the pointers of
    # the link's next and prev to point to each other. This means that
    # nothing is pointing to this link and it is thus garbage-collected
    def remove(self):
        prev_link = self.prev
        next_link = self.next
        prev_link.next = next_link
        next_link.prev = prev_link


    # String representation for a link - e.g. str(link). Useful for
    # debugging
    def __str__(self):
        return "[" + repr(self.key) + ", " + repr(self.val) + "]"
