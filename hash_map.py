from linked_list import LinkedList

class HashMap(object):

    def __init__(self, num_buckets=None):
        if num_buckets is None:
            num_buckets = 8


        self.store = [LinkedList()] * num_buckets
        self.count = 0


    def include(self, key):
        linked_list = self.store[hash(key) % len(self.store)]

        return linked_list.include(key)

    def set(self, key, val):
        linked_list = self.store[hash(key) % len(self.store)]

        if self.include(key):
            linked_list.update(key, val)
        else:
            if self.count == len(self.store):
                self.resize()
            linked_list.append(key, val)
            self.count = self.count + 1

    def get(self, key):
        return self.store[hash(key) % len(self.store)].get(key)

    def delete(self, key):
        linked_list = self.store[hash(key) % len(self.store)]

        if linked_list.include(key):
            linked_list.remove(key)
            self.count = self.count - 1

    def resize(self):
        old_store = self.store
        self.count = 0
        self.store = [LinkedList()] * (len(self.store))

        for linked_list in old_store:
            for link in linked_list:
                self.set(link.key, link.val)

def hashMaker ():
    some_hash = HashMap()
    some_hash.set("first", 1)
    some_hash.set("second", 2)
    some_hash.set("third", 3)
    return some_hash
