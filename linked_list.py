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






empty_list = LinkedList()
print(empty_list.empty() == True)

linked_list = LinkedList()
linked_list.append("first", 1)
linked_list.append("second", 2)
linked_list.append("third", 3)

print(linked_list.empty() == False)

empty_list.append("first", 1)
print(empty_list.empty() == False)

print(linked_list.first().key == "first")
print(linked_list.last().key == "third")

# Another test
empty_list_2 = LinkedList()
empty_list_2.append("first", 1)
empty_list_2.update("first", 2)
print("updates links")
print(empty_list_2.first().val == 2)

# Another test
print("doesn't add new links")
empty_list_3 = LinkedList()
empty_list_3.update("first", 2)
print(empty_list_3.empty() == True)

print("get")
print("gets by key")
linked_list_2 = LinkedList()
linked_list_2.append("first", 1)
linked_list_2.append("second", 2)
linked_list_2.append("third", 3)
print(linked_list_2.get("first") == 1)
print(linked_list_2.get("second") == 2)
print(linked_list_2.get("third") == 3)

print("returns nil for absent keys")
print(linked_list_2.get("absent key") == None)

print("remove")
print("removes a link by key")
linked_list_3 = LinkedList()
linked_list_3.append("first", 1)
linked_list_3.append("second", 2)
linked_list_3.append("third", 3)

print(linked_list_3.get("first") == 1)
linked_list_3.remove("first")
print(linked_list_3.get("first") == None)


print("reassigns pointers when links are removed")
linked_list_4 = LinkedList()
linked_list_4.append("first", 1)
linked_list_4.append("second", 2)
linked_list_4.append("third", 3)
linked_list_4.remove("second")
print(linked_list_4.first().next.key == "third")
print(linked_list_4.last().prev.key == "first")

print("include")
print("returns true if a key is present")
linked_list_5 = LinkedList()
linked_list_5.append("first", 1)
linked_list_5.append("second", 2)
linked_list_5.append("third", 3)
print(linked_list_5.include("first") == True)

print("returns false if a key is not in the list")
print(linked_list_5.include("fourth") == False)
