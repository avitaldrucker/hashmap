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

print("")
print("HASH MAP")
print("[]")
print("gets by key")
some_hash = hashMaker()
print(some_hash.get("first") == 1)
print(some_hash.get("second") == 2)
print(some_hash.get("third") == 3)


print("")
print("[]=")
some_hash_1 = hashMaker()
print('sets a key value pair')
some_hash_1.set("fourth", 4)
print(some_hash_1.get(4) == None)
print(some_hash_1.get("fourth") == 4)

print("overwrites any existing value for the given key")
some_hash_2 = hashMaker()
some_hash_2.set("one", 1)
some_hash_2.set("one", "one")
print(some_hash_2.get("one") == "one")

print("works with various data types")
some_hash_3 = hashMaker()
some_hash_3.set("fourth", 4)
some_hash_3.set(5, 5)
print(some_hash_3.get("fourth") == 4)
print(some_hash_3.get(5) == 5)

print("")
print("include")
print("returns true if a key is present")
some_hash_4 = hashMaker()
print(some_hash_4.include("first") == True)

print("returns false if a key is not in the hash")
print(some_hash_4.include("fourth") == False)

print("")
print("deletes keys")
some_hash_5 = hashMaker()
print(some_hash_5.get("first") == 1)
some_hash_5.delete("first")
print(some_hash_5.get("first") is None)

print("")
print("count")
print("keeps count through insertions")
some_hash_6 = hashMaker()
print(some_hash_6.count == 3)
print("does not change count when updating existing key")
some_hash_7 = hashMaker()
some_hash_7.set("first", 1)
print(some_hash_7.count == 3)
print("keeps count through deletions")
some_hash_8 = hashMaker()
some_hash_8.delete("first")
print(some_hash_8.count == 2)

print("")
print("resize")
