class Link(object):

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

link = Link()
print(link.key)
print(link.val)
print(link.next)
print(link.prev)
print(link.to_s)


# class MyStuff(object):
#
#     def __init__(self):
#         self.tangerine = "And now a thousand years between"
#
#     def apple(self):
#         print "I AM CLASSY APPLES!"
#
#
#         def append_to(element, to=None):
#     if to is None:
#         to = []
#     to.append(element)
#     return to
