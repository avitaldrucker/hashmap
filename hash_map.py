from linked_list import LinkedList


class HashMap(object):


    def __init__(self, num_buckets=None):
        if num_buckets is None:
            num_buckets = 8

        self.store = []

        while len(self.store) < num_buckets:
            self.store.append(LinkedList())

        self.count = 0


    def include(self, key):
        return self.bucket(key).include(key)


    def __getitem__(self, key):
        return self.bucket(key).get(key)


    def __setitem__(self, key, val):
        linked_list = self.bucket(key)

        if self.include(key):
            linked_list.update(key, val)
        else:
            if self.count == len(self.store):
                self.resize()
            linked_list.append(key, val)
            self.count = self.count + 1


    def set(self, key, val):
        self[key] = val


    def get(self, key):
        return self[key]


    def delete(self, key):
        linked_list = self.bucket(key)

        if linked_list.include(key):
            linked_list.remove(key)
            self.count -= 1


    def resize(self):
        old_store = self.store
        self.count = 0
        self.store = []

        while len(self.store) < len(old_store) * 2:
            self.store.append(LinkedList())

        for linked_list in old_store:
            link = linked_list.first()
            while link != linked_list.tail:
                self[link.key] = link.val
                link = link.next


    def bucket(self, key):
        return self.store[hash(key) % len(self.store)]


    def __str__(self):
        pairs = []

        i = 0

        while i < len(self.store):
            linked_list = self.store[i]
            if not linked_list.empty():
                pairs.append(str(linked_list))

            i = i + 1

        return ", ".join(pairs)
